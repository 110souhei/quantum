from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import matplotlib.pyplot as plt
import numpy as np
from Hadamard_test import Hadamard_test
from vector import vector


def cal(n,a,the,phi,lam,gam,im):
# Create a new circuit with two qubits
    s = 10000
    qc = QuantumCircuit(n+1,1)
    qc = qc.compose(vector(n,a))
    qc = qc.compose(Hadamard_test(n,the,phi,lam,gam,im))# Hadamard_test

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
    print(counts)
    try:
        res = counts['0']
    except KeyError:
        res = 0
    return res


if __name__ == "__main__":
    ans = np.zeros(100)
    the = 0
    phi = 0
    lam = np.pi
    gam = 0
    for i in range(100):
        a = np.array([99-i,i])
        print(a)
        ans[i] = cal(1,a,the,phi,lam,gam,True)/10000
    print(ans)
    plt.plot(ans)
    plt.show()