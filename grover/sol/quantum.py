from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np

c

# Create a new circuit with two qubits
def quantum(json_input):

    n = int(json_input["nqbit"])
    a = np.array(json_input["a"])
    s = json_input["shot"]

    qc = QuantumCircuit(n,n)
    

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
    "f": [
        [0,1,-2],[-1]
    ],
    "seed": 959
    } 
    print(quantum(json_input))
