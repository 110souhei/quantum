import numpy as np

n = 16
seed = (int(input()))
np.random.seed(seed)

print(n)
for i in range(2):
    a = np.zeros(0)
    for j in range(2**n):
        a = np.append(a,np.random.rand())
    a_l2_norm = sum(abs(a)**2)**0.5
    a = a/a_l2_norm
    for j in range(2**n):
        print(a[j],end=' ')
    print()