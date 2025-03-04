import json
import sys
import random
import os
import numpy as np
from gen.random_real import maker



def main():
    f = open('info.json','r')
    json_dict = json.load(f)
    print(type(json_dict))
    json_gen = json_dict['gen']
    np.random.seed(json_gen["seed"])
    for nqbit in json_gen["real"]["qbit"]:
        dirname = f"in/random_real/qbit_{nqbit}"
        os.makedirs(dirname, exist_ok = True)
        for i in range(json_gen["real"]["case"]):
            est = {}
            est["nqbit"] = nqbit
            est["seed"] = int(np.random.default_rng().integers(1000))
            input_case = maker(est)
            print(input_case)
            with open(f"{dirname}/{i}.in", 'w') as f2:
            #with open('nyanya','w') as f2:
                json.dump(input_case, f2, indent=4)

if __name__ == "__main__":
    main()

