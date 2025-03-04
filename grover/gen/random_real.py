import numpy as np
import json

def maker(est):
    n = est["nqbit"]
    seed = est["seed"]
    np.random.seed(seed)
    
    res = {}
    res["nqbit"] = n
    a = np.zeros(2**n)
    for i in range(2**n):
        a[i] = np.random.rand()
    a_l2_norm = sum(abs(a)**2)**0.5
    a = a/a_l2_norm
    res["a"] = a.tolist()
    res["seed"] = seed
    return res

def main():
    est = {}
    #test
    est["nqbit"] = 2
    est["seed"] = 10
    f = maker(est)
    print(f)

if __name__ == "__main__":
    main()
