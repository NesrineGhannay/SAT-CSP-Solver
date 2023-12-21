from pycsp3 import *

data = (10, 3)

n = data[0]
k = data[1]

b = VarArray(size=n, dom=range(1, k + 1))

satisfy(
    (imply(b[i] == b[j], b[l] != b[i]))
    for i in range(n) for j in range(n) for l in range(n)
    if (i + j == l)
)

result = solve()

print(result)