from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np
from swap_test import swap_test
from vector import vector

# Create a new circuit with two qubits
n = int(input())
a = np.array(list(map(float,input().split())))
b = np.array(list(map(float,input().split())))
s = 1000

qc = QuantumCircuit(2*n+1,1)
qc = qc.compose(vector(n,a,b))
qc = qc.compose(swap_test(n))

sim = StatevectorSimulator()
job = sim.run(qc)
result = job.result()
state = result.get_statevector()
#print(result)
#print(state)


#print(qc)

q_sim = QasmSimulator()
job = q_sim.run(qc,shots=s)
result = job.result()
counts = result.get_counts()
#print(counts)
print(( (counts['0']/s)*2 - 1)**0.5)