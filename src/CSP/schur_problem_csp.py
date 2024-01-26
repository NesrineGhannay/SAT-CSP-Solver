import time

from pycsp3 import *
from timeout_decorator import timeout, TimeoutError


@timeout(600)
def generate_schur_csp_instance(k, n):
    b = VarArray(size=n, dom=range(1, k + 1))

    satisfy(
        ((b[i] != b[j]) | (b[i] != b[l]) | (b[j] != b[l]))
        for i in range(1, n+1) for j in range(i + 1, n+1) for l in range(j+1, n+1)
        if (i + j == l)
    )

    if solve() is SAT:
        return values(b)
    else:
        print("l'instance n'a pas de solution")
        return "NO SOLUTION"


def show_solution(solution):
    max_k = max(solution)
    resultat = ""
    for k in range(1, max_k + 1):
        #resultat += "Boite " + str(k) + " : "
        for n in range(1, len(solution) + 1):
            if solution[n] == k:
                resultat += " " + str(n)
        resultat += '\n'
    print(resultat)

#valeurs = generate_schur_csp_instance(3, 4)
startTime = time.time()
valeurs = generate_schur_csp_instance(5, 170)
endTime = time.time()
print(endTime - startTime, " s.")
#valeurs = generate_schur_csp_instance(4, 100)
#valeurs = generate_schur_csp_instance(5, 140)
#valeurs = generate_schur_csp_instance(5, 150)
#valeurs = generate_schur_csp_instance(5, 160)
#valeurs = generate_schur_csp_instance(5, 170)


if valeurs != "NO SOLUTION":
    #print(valeurs)
    show_solution(valeurs)
