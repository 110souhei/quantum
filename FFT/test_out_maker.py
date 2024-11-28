import json
import sys
import random
import os
import numpy as np
from gen.random_real import maker
from sol.classic import classic


def make_output(input_name,case_number):
    f = open("in/{input_name}/{case_number}.in",'r')
    json_input = json.load(f)
    ######
    res = classic(f)
    f2 = open("out/classic/{input_name}/{case_number}.out",'w')
        json.dump(res,f2,indent=4)



main():
    f = open('info.json','r')
    json_dict = json.load(f)
    print(type(json_dict))
    json_gen = json_dict['gen']
    #json_sol = json_dict['sol'] 工事中　ファイル名からプログラムをインポートしたい

    np.random.seed(json_gen["seed"])
    for nqbit in json_gen["real"]["qbit"]:
        dirname = f"in/random_real/qbit_{nqbit}"
        for i in range(json_gen["real"]["case"]):
            ####
            input_name = dirname + i + ".in"
            print(input_name,json_sol)
            with open(input_name, 'r') as f2:
            #with open('nyanya','w') as f2:
                json.dump(input_case, f2, indent=4)

if __name__ == "__main__":
    main()

