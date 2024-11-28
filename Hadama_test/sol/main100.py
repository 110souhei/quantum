from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np
from QFFT import QFFT
from vector import vector
 
# Create a new circuit with two qubits
n = int(input())
a = np.array(list(map(float,input().split())))

s = 100

qc = QuantumCircuit(n,n)
qc = qc.compose(vector(n,a))
qc = qc.compose(QFFT(n))

sim = StatevectorSimulator()
job = sim.run(qc)
result = job.result()
state = result.get_statevector()
#print(result)
print(state)


print(qc)


qc.measure_all()
q_sim = QasmSimulator()
job = q_sim.run(qc,shots=s)
result = job.result()
counts = result.get_counts()
print(counts)