import numpy as np

def dft_(f):
    n = len(f)
    Y = np.arange(n,dtype = complex)
    for x in range(n):
        y = complex(0,0)
        for t in range(n):
            a = 2 * np.pi * t * x / n
            y += f[t]* np.e**(1j*a)/(np.sqrt(n))
        Y[x] = y
    return Y

def classic(json_input):
    n = int(json_input["nqbit"]) # n- qubit 
    a = np.array(json_input["a"])
    y = dft_(a)

    res = {}
    res["state"] = y.tolist()
    return res


if __name__ == "__main__":
    json_input ={
    "nqbit": 2,
    "a": [
        0.5179274908910946,
        0.6418741294413983,
        0.38972529335552286,
        0.4097107660924397
    ],
    "seed": 959
    } 
    print(classic(json_input))
    
