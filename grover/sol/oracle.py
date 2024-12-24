from qiskit import QuantumCircuit
from qiskit_aer import StatevectorSimulator,QasmSimulator
import numpy as np


def oracle(n: int,l: int,f: dict)-> QuantumCircuit:
    qc = QuantumCircuit(n+l+1)

    def adder_gate(r : bool):
        k = 0
        for i in f:
            a = []
            for j in range(n):
                if(i[j] == 0):
                    a.append(j)
                elif(i[j] == 1):
                    qc.x(j)
                    a.append(j)
            if(len(a) == 0):
                continue
            if(not(r)):
                qc.mcx(a,n+k)
            else:
                qc.mcx(a,n+(l-1-k))
            k+=1
            for j in range(n):
                if(i[j] == 1):
                    qc.x(j)
    
    adder_gate(False)
    qc.x(range(n,n+l,1))
    qc.mcx(list(range(n,n+l,1)),n+l)
    qc.x(range(n,n+l,1))

    f.reverse()
    adder_gate(True)
    
    return qc

if __name__ == "__main__":
    f = [[1,1,-1,0],[-1,0,1,1]]
    qc = oracle(4,2,f)
    s = int(10000)
    print(qc)
    qc.measure_all()
    q_sim = QasmSimulator()
    job = q_sim.run(qc,shots=s)
    result = job.result()
    counts = result.get_counts()
    print(counts)