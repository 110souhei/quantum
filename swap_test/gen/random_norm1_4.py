import numpy as np

n = 4
seed = (int(input()))
np.random.seed(seed)

print(n)
for i in range(2):
    a = np.zeros(0)
    for i in range(2**n):
        a = np.append(a,np.random.rand())
    a_l2_norm = sum(abs(a)**2)**0.5
    a = a/a_l2_norm
    for i in range(2**n):
        print(a[i],end=' ')
    print()