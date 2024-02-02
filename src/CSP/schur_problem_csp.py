import time
from pycsp3 import *
from timeout_decorator import timeout, TimeoutError

@timeout(600)
def generate_schur_csp_instance(k, n):
    """
    Génère une instance du problème Schur CSP et tente de trouver une solution.

    :param k: Nombre de boîtes
    :param n: Nombre de balles
    :return: Liste des valeurs associées à chaque balle si une solution est trouvée, sinon "NO SOLUTION"
    """
    # Crée un tableau de variables représentant la balle associée à chaque balles
    b = VarArray(size=n, dom=range(1, k + 1))

    # Définit les contraintes CSP pour le problème Schur
    satisfy(
        ((b[i] != b[j]) | (b[i] != b[l]) | (b[j] != b[l]))
        for i in range(1, n+1) for j in range(i + 1, n+1) for l in range(j+1, n+1)
        if (i + j == l)
    )

    # Résout le problème CSP
    if solve() is SAT:
        return values(b)
    else:
        print("L'instance n'a pas de solution")
        return "NO SOLUTION"

def show_solution(solution):
    """
    Affiche la solution du problème Schur CSP.

    :param solution: Liste des valeurs associées à chaque balle
    """
    max_k = max(solution)
    resultat = ""
    for k in range(1, max_k + 1):
        for n in range(1, len(solution) + 1):
            if solution[n] == k:
                resultat += " " + str(n)
        resultat += '\n'
    print(resultat)

# Mesure le temps d'exécution de la génération et de la résolution de l'instance CSP
startTime = time.time()
valeurs = generate_schur_csp_instance(3, 20)
endTime = time.time()
print(endTime - startTime, " s.")

# Affiche la solution si elle existe
if valeurs != "NO SOLUTION":
    show_solution(valeurs)
