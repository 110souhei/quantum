from qiskit import QuantumCircuit
import numpy as np


def Hadamard_test(n,the,phi,lam,gam,im) -> QuantumCircuit:
    qc = QuantumCircuit(n+1)
    qc.h(0)
    if(im == True):
        qc.p(np.pi*(3/2),0)
    qc.cu(the,phi,lam,gam,0,1)
    qc.h(0)
    return qc