#まずはprocedualに
import matplotlib.pyplot as plt
from random import uniform
fig, ax = plt.subplots()

n = 1000 #the count of repeat
x0 = [uniform(0, 1)]
x1 = [uniform(0, 1)]
s = ((1,-1),(-1,1),(-1,1),(1,-1)) #利得行列

for i in range(n-1):
    if (s[0][0]*x0[i]+s[1][0]*(1-x0[i]) > s[2][0]*x0[i]+s[3][0]*(1-x0[i])):
        a0 = 0
    elif (s[0][0]*x0[i]+s[1][0]*(1-x0[i]) < s[2][0]*x0[i]+s[3][0]*(1-x0[i])):
        a0 = 1
    else:
        a0 = 0 #本当はランダムで0か1
    
    if (s[0][1]*x1[i]+s[2][1]*(1-x1[i]) > s[1][1]*x1[i]+s[3][1]*(1-x1[i])):
        a1 = 0
    elif (s[0][1]*x1[i]+s[2][1]*(1-x1[i]) < s[1][1]*x1[i]+s[3][1]*(1-x1[i])):
        a1 = 1
    else:
        a1 = 0 #本当はランダムで0か1

    x0.append(x0[i]+(a1-x0[i])/(i+2))
    x1.append(x1[i]+(a0-x1[i])/(i+2))
ax.plot(x0, 'r-')
ax.plot(x1, 'b-')
plt.show()

#if文の中身をObjectにして裏で動かすとObject指向らしくなる

