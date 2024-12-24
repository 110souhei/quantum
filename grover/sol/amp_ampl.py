from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np

def amp_ampl(n: int,l: int)-> QuantumCircuit:
    qc = QuantumCircuit(n+l+1)
    qc.h(range(n))
    qc.x(range(0,n,1))
    qc.mcx(list(range(0,n,1)),l+n)
    qc.x(range(0,n,1))
    qc.h(range(n))
    return qc