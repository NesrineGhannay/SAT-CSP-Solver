from pycsp3 import *


def generate_schur_csp_instance(n, k):
    b = VarArray(size=n, dom=range(1, k + 1))

    satisfy(
        ((b[i] != b[j]) | (b[i] != b[l]) | (b[j] != b[l]))
        for i in range(n) for j in range(n) for l in range(n)
        if (i + j == l)
    )

    if solve() is SAT:
         return values(b)
    else :
        print("l'instance n'a pas de solution")
        return "NO SOLUTION"


def show_solution(solution):
    max_k = max(solution)
    resultat = ""
    for k in range(1, max_k + 1):
        resultat += "Boite " + str(k) + " : "
        for n in range(1, len(solution) + 1):
            if solution[n] == k:
                resultat += " " + str(n)
        resultat += '\n'
    print(resultat)



valeurs = generate_schur_csp_instance(20, 4)
if valeurs != "NO SOLUTION":
    show_solution(valeurs)


