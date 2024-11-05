import os
import glob

a = glob.glob('../out/4/classic/*.out')
b = glob.glob('../out/4/quantum')
classic = np.zeros(10)
quantum = np.zero(10)
print(a)
for i in a:
    print(i)
    with open(i) as f:
        b = float(f.read())
        print(b)
