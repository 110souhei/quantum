from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_state_city
from qiskit_aer import StatevectorSimulator,QasmSimulator
from scipy.optimize import minimize
import numpy as np
def get_cost_circuit(N : int, G : np.ndarray, gamma : np.double) -> QuantumCircuit:
    qc = QuantumCircuit(N,N)
    for c in G:
        qc.cx(c[0],c[1])
        qc.rz(gamma,c[1])
        qc.cx(c[0],c[1])
    return qc
def get_mixer_circuit(N : int, beta: np.double) -> QuantumCircuit:
    qc = QuantumCircuit(N,N)
    for j in range(N):
        qc.rx(2*beta,j)
    return qc
def get_qaoa_circuit(N : int, G : np.ndarray, beta: np.ndarray, gamma: np.ndarray) -> QuantumCircuit:
    p = len(beta)
    qc = QuantumCircuit(N,N)
    qc.h([i for i in range(N)])
    for i in range(p):
        qc.compose(get_cost_circuit(N,G,gamma[i]), inplace = True)
        qc.compose(get_mixer_circuit(N,beta[i]), inplace = True)
    return qc
def cal_cost(N: int, G: np.ndarray,count, shots : float) -> float:
    res = 0.0
    for i in count:
        #print(i)
        for c in G:
            #print(c)
            #print(i[c[0]] + " " + i[c[1]])
            if(i[c[0]] != i[c[1]]):
                res = res + count[i]
    return res/shots


def get_objective(theta: np.ndarray,N : int , G: np.ndarray) -> float:
    shots = 1000000
    p = int(len(theta) / 2)
    beta = theta[:p]
    gamma = theta[p:]
    qc = get_qaoa_circuit(N,G,beta,gamma)
    qc.measure_all()
    #print(beta)
    #print(gamma)
    #print(qc)
    sim = StatevectorSimulator()
    #print(sim)
    job = sim.run(qc,shots=shots)
    result = job.result()
    count = result.get_counts()
    #print(result)
    cost = cal_cost(N, G , count, shots)
    #print(cost)
    #print("end one prosess")
    return -cost


def optimize_qaoa(N : int, G : np.ndarray):
    OPTIONS = {"maxiter" : 10000, "disp": True}
    ARGS = (N,G)
    betagamma = np.zeros(1*2)
    result_xs = []
    result_its = []
    result_nfev = []
    result_val = []
    for i in range(10):
        result = minimize(get_objective,x0 =  betagamma, method= "Nelder-Mead", args = ARGS, options = OPTIONS, tol = 1e-2)
        result_xs.append(result.x)
        result_its.append(result.nit)
        result_nfev.append(result.nfev)
        result_val.append(result.fun)
    

    print(result_xs)
    print(result_its)
    print(result_nfev)
    print(result_val)


if __name__ == "__main__":
    N1 = 5
    G1 = np.array([[0,1],[1,2],[2,3],[3,4],[2,4]])
    optimize_qaoa(N1,G1)
    
    #print("#######")
    
    #N2 = 4
    #G2 = np.array([0,1],[1,2],[2,3],[0,3])
    
    #optimize_qaoa(N2,G2)
    #print("########")
    #N3 = 4
    #G3 = np.array([0,1],[1,2],[2,3],[0,3],[0,2])
    #optimize_qaoa(N3,G3)
    
    