from qiskit import QuantumCircuit
import numpy as np
#nlogn -> inic
#回路構築の時間は？
#量子状態準備


def vector(n,a) -> QuantumCircuit: # n-qbit 
    
    qc = QuantumCircuit(n+1)
    a_l2_norm = sum(abs(a)**2)**0.5
    a = a/a_l2_norm

    qc.initialize(a,range(1,n+1,1))
    return qc