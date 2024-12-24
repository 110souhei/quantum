from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np
from oracle import oracle
from amp_ampl import amp_ampl



# Create a new circuit with two qubits
def quantum(json_input):

    n = int(json_input["nqbit"])
    s = json_input["shot"]
    f = json_input["f"]
    l = json_input["l"]
    m = json_input["m"]
    qc = QuantumCircuit(n+l+1,n)
    
    qc.x(n+l)
    qc.h(n+l)
    qc.h(range(n))
    for i in range(m):
        print(i)
        qc = qc.compose(oracle(n,l,f))
        qc.barrier()
        qc = qc.compose(amp_ampl(n,l)) 

    res = {}
    sim = StatevectorSimulator()
    job = sim.run(qc)
    result = job.result()
    state = result.get_statevector()
    #print(result)
    print(state)


    print(qc)


    qc.measure(range(2),range(2))
    q_sim = QasmSimulator()
    job = q_sim.run(qc,shots=s)
    result = job.result()
    counts = result.get_counts()
    print(counts)
    res["counts"] = counts
    res["shot"] = s 
    return res

if __name__ == "__main__":
    json_input ={
    "nqbit": 4,
    "shot":10000,
    "m" : 1,
    "l":10,
    "f": [
        [1,1,-1,1],[1,0,-1,1],[0,0,-1,0],[1,-1,0,0],[0,0,0,-1],[-1,0,1,1],[0,1,0,-1],[-1,0,1,0],[-1,1,1,0],[1,-1,0,1]],
    "seed": 959
    } 
    quantum(json_input)
