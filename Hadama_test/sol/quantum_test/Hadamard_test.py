from qiskit import QuantumCircuit
import numpy as np


def Hadamard_test(n) -> QuantumCircuit:
    qc = QuantumCircuit(n+1)
    qc.h(0)
    qc.cu(0,0,0,0,0,1)
    qc.h(0)
    return qc