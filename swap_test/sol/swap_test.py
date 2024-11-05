from qiskit import QuantumCircuit

def swap_test(n) -> QuantumCircuit:


    qc = QuantumCircuit(2*(n) + 1,1)

    qc.h(0)
    for i in range(n):
        qc.cswap(0,i+1,i+1+n)
    qc.h(0)
    qc.measure([0],[0])

    return qc