from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np
from Hadamard_test import Hadamard_test




def main():
# Create a new circuit with two qubits
    n = 1
    s = 100
    qc = QuantumCircuit(n+1,1)
    qc = qc.compose(Hadamard_test(n))


    sim = StatevectorSimulator()
    job = sim.run(qc)
    result = job.result()
    state = result.get_statevector()
    #print(result)

    print(state)
    print(qc)
    qc.measure(0,0)
    q_sim = QasmSimulator()
    job = q_sim.run(qc,shots=s)
    result = job.result()
    counts = result.get_counts()
    print(counts['0']/s)

if __name__ == "__main__":
    main()