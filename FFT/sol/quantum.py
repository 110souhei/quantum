from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
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
        qc.swap(i,n-i-1)
    return qc

def vector(n,a) -> QuantumCircuit: # n-qbit 
    
    qc = QuantumCircuit(n)
    a_l2_norm = sum(abs(a)**2)**0.5
    a = a/a_l2_norm

    qc.initialize(a,range(0,n,1))
    return qc

# Create a new circuit with two qubits
def quantum(json_input):

    n = int(json_input["nqbit"])
    a = np.array(json_input["a"])
    s = json_input["shot"]

    qc = QuantumCircuit(n,n)
    qc = qc.compose(vector(n,a))
    qc = qc.compose(QFFT(n))

    sim = StatevectorSimulator()
    job = sim.run(qc)
    result = job.result()
    state = result.get_statevector()
    #print(result)
    res = {}
    temp = {}
    temp["real"] = [0]*len(state)
    temp["imag"] = [0]*len(state)
    for i in range(len(state)):
        temp["real"][i] = float(state[i].real)
        temp["imag"][i] = float(state[i].imag)
    res["state"] = temp
    #print(state)
    #print(temp)


    #print(qc)


    qc.measure_all()
    q_sim = QasmSimulator()
    job = q_sim.run(qc,shots=s)
    result = job.result()
    counts = result.get_counts()
    #print(counts)
    res["counts"] = counts
    res["shot"] = s 
    return res

if __name__ == "__main__":
    json_input ={
    "nqbit": 2,
    "shot":100,
    "a": [
        0.5179274908910946,
        0.6418741294413983,
        0.38972529335552286,
        0.4097107660924397
    ],
    "seed": 959
    } 
    print(quantum(json_input))
