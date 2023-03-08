from RandomNumberGenerator import *

rng = RandomNumberGenerator(1)
p = []
for _ in range(1,11):
    p.append(rng.nextInt(1,29))
print(p)
A = sum(p)
r = []
for _ in range(1,11):
    r.append(rng.nextInt(1,A))
print(r)

pi = [i for i in range(1,11)]
print(pi)
S = []
C = []

a = list(zip(r, p))
a.sort(key=lambda x: x[0])

def evaluate(p,r,pi):
    for i in range(0,10):
      if(i == 0):
          S.append(r[i])
      else:
          S.append(max(r[i], C[i-1]))

      C.append(S[i]+p[i])

ar = [x[0] for x in a]
ap = [x[1] for x in a]

evaluate(ap,ar,pi)
print(C)
print(max(C))
print(S)