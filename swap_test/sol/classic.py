import numpy as np

n = int(input())
a = np.array(list(map(float,input().split())))
b = np.array(list(map(float,input().split())))

ans = 0
for i in range(2**n):
    ans = ans + (a[i]*(b[i]))

print(ans)
