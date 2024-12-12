from qiskit import QuantumCircuit
import numpy as np

def QFFT(n) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    for j in range(n):
        qc.h(j)
        for k in range(j+1,n):
            a = 2*np.pi*j/(2**k)
            #print(str(j) + " " + str(k) + " " + str(a))
            qc.cp(a,k,j)
    for i in range(n//2):
        print(str(i) + " " + str(n-1-i))
        qc.swap(i,n-i-1)
    return qc