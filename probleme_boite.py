from pycsp3 import *

n = data[0]
k = data[1]

b = VarArray(size=n, dom=range(1, k + 1))

satisfy(
    (imply(b[i] == b[j], b[l] != b[i]))
    for i in range(n + 1) for j in range(n + 1) for l in range(n + 1)
    if (i + j == l)
)
