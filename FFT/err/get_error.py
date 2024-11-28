import os
import glob
import numpy as np

a = glob.glob('../out/4/classic/*.out')
shot4 = [glob.glob('../out/4/quantum/shot100/*.out'),glob.glob('../out/4/quantum/shot1000/*out'),glob.glob('../out/4/quantum/shot10000/*.out')]
classic = np.zeros(10)
quantum = np.zeros((3,10))

count = 0
print(a)
for i in a:
    print(i)
    with open(i) as f:
        c = float(f.read())
        classic[count] = c
        count+=1


for a in range(3):
    count = 0
    for i in shot4[a]:
        print(i)
        with open(i) as f:
            c = float(f.read())
            quantum[a][count] = c
            count+=1

for i in range(10):
    print(str(classic[i]) + " " + str(quantum[0][i]) + " " + str(quantum[1][i]) + " " + str(quantum[2][i]))

err_ave = np.zeros(3)

for i in range(3):
    for j in range(10):
        err_ave[i] = abs(classic[j]-quantum[i][j])
    err_ave[i]/=10
print("絶対誤差の平均")
print(str(err_ave[0])+" "+str(err_ave[1])+" "+str(err_ave[2]))
"相対誤差を取ろう"
"分散、標準偏差"