#まずはprocedualに
import matplotlib.pyplot as plt
import numpy as np
from random import uniform
fig, ax = plt.subplots()

n = 1000 #the count of repeat
s = ((1,-1),(-1,1),
     (-1,1),(1,-1)) #利得行列

x0 = [uniform(0, 1)]
x1 = [uniform(0, 1)]

def ss(a, s):
    return ((s[0][a], s[1][a]),
            (s[2][a], s[3][a]))

s0 = np.array(ss(0, s))
s1 = np.array(ss(1, s))

for i in range(n-1):
    vec0 = (1-x0[i], x0[i])
    vec1 = (1-x1[i], x1[i])

    A0 = np.dot(s0, vec0)
    A1 = np.dot(s1, vec1)
    a0 = A0.argmax() #同じだったときのrandomが表現できず少し不正確
    a1 = A1.argmax()

    x0.append(x0[i]+(a1-x0[i])/(i+2))
    x1.append(x1[i]+(a0-x1[i])/(i+2))
ax.plot(x0, 'r-')
ax.plot(x1, 'b-')
plt.show()
#if文の中身をObjectにして裏で動かすとObject指向らしくなる