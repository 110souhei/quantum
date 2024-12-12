from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np

def amp_ampl(n: int)-> QuantumCircuit:
    qc = QuantumCircuit(n)
    qc.h(range(n))
    if(n == 1):
        qc.z(0)
    else:
        qc.append(Zgate().control(n-1),range(n))
    qc.h(range(n))
    return qc