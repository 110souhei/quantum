from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np


def oracle(n: int,f: dict)-> QuantumCircuit:
