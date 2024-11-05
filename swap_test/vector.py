from qiskit import QuantumCircuit
import numpy as np
#nlogn -> inic
#回路構築の時間は？
#量子状態準備


def vector(n,a,b) -> QuantumCircuit:
    
    qc = QuantumCircuit(2*(2**(n-1))+1)
    print(type(a)) 
    a_l2_norm = sum(abs(a)**2)**0.5
    a = a/a_l2_norm
    b_l2_norm = sum(abs(b)**2)**0.5
    b = b/b_l2_norm


    #for i in a:
    #    print((i**2)*1000,end=" ")
    #print()
    #print(a)
    qc.initialize(a,range(1,n+1,1))
    qc.initialize(b,range(n+1,2*n+1,1))
    return qc