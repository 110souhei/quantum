import json
import sys
import random
import os
import numpy as np
from gen.random_real import maker
from sol.classic import classic
#from sol.quantum import quantum



def make_output_classic(input_name):
    f = open(f"in/{input_name}.in",'r')
    json_input = json.load(f)
    ######
    res = classic(json_input)
    print("open")
    print(f"out/classic/{input_name}.out")
    f2 = open(f"out/classic/{input_name}.out",'w')
    print(res)
    json.dump(res,f2,indent=4)

'''
def make_output_quantum(input_name,case_number,shot):
    f = open("in/{input_name}/{case_number}.in",'r')
    json_input = json.load(f)
    json_input["shot"] = shot
    ######
    res = classic(f)
    f2 = open("out/classic/{shot}/{input_name}/{case_number}.out",'w')
        json.dump(res,f2,indent=4)
'''


def main():
    f = open('info.json','r')
    json_dict = json.load(f)
    print(type(json_dict))
    json_gen = json_dict['gen']
    #json_sol = json_dict['sol'] 工事中　ファイル名からプログラムをインポートしたい

    np.random.seed(json_gen["seed"])
    for nqbit in json_gen["real"]["qbit"]:
        dirname = f"random_real/qbit_{nqbit}/"

        # classic
        out_f = f"out/classic/{dirname}"
        print(out_f)
        os.makedirs(out_f,exist_ok = True)
        for i in range(json_gen["real"]["case"]):
            input_name = dirname + str(i)
            print(input_name + ".in")
            make_output_classic(input_name)

if __name__ == "__main__":
    main()

