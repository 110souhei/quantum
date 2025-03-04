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
    #print(len(count))
    for i in range(len(count)):
        t = (count[i].real ** 2 + count[i].imag**2)
        for c in G:
            if((i>>c[0])&(1) != (i>>c[1])&(1)):
                res += t
    return res

def get_objective(theta: np.ndarray,N : int , G: np.ndarray) -> float:
    shots = 10000
    p = int(len(theta) / 2)
    beta = theta[:p]
    gamma = theta[p:]
    qc = get_qaoa_circuit(N,G,beta,gamma)
    qc.measure_all()
    print("AAAAAAAAAAAAAAAAA")
    qc.draw()
    #print(beta)
    #print(gamma)
    #print(qc)
    sim = StatevectorSimulator()
    #print(sim)
    job = sim.run(qc)
    result = job.result().get_statevector()
    #print("result")
    #print(result)
    #print(type(result))
    cost = cal_cost(N, G , result, shots)
    #print(cost)
    return -cost


def optimize_qaoa(N : int, G : np.ndarray):
    OPTIONS = {"maxiter" : 10000}#, "disp": True}
    ARGS = (N,G)
    betagamma = np.zeros(2*2)
    result_xs = []
    result_its = []
    result_nfev = []
    result_val = []
    for i in range(100):
        result = minimize(get_objective,x0 =  betagamma, method= "Nelder-Mead", args = ARGS, options = OPTIONS, tol = 1e-3)
        result_xs.append(result.x)
        result_its.append(result.nit)
        result_nfev.append(result.nfev)
        result_val.append(result.fun)
    

    print(result_xs)
    print(result_its)
    print(result_nfev)
    print(result_val)


if __name__ == "__main__":
    N = 5
    M = 5
    G = np.array([[0,1],[1,2],[2,3],[3,4],[2,4]])
    optimize_qaoa(N,G)

    
    print("#######")
    
    N2 = 4
    G2 = np.array([[0,1],[1,2],[2,3],[0,3]])
    
    optimize_qaoa(N2,G2)
    print("########")
    N3 = 4
    G3 = np.array([[0,1],[1,2],[2,3],[0,3],[0,2]])
    optimize_qaoa(N3,G3)
    
    