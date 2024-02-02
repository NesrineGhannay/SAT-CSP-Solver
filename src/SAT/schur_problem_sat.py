def generate_schur_sat_instance(k, n):
    """
    Génère une instance de problème Schur SAT sous forme de clauses.

    :param k: Nombre de boîtes
    :param n: Nombre de balles
    :return: Clauses au format CNF
    """
    clauses = ""

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for l in range(j + 1, n + 1):
                if i + j == l:
                    for m in range(1, k + 1):
                        clauses += str(formeInjective(-i, -m, k)) + " " + str(formeInjective(-j, -m, k)) + " " + str(
                            formeInjective(-l, -m, k)) + " 0\n"

    for i in range(1, n + 1):
        clause = ""
        for j in range(1, k + 1):
            clause += str(formeInjective(i, j, k)) + " "
        clauses += clause + "0\n"

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(j + 1, k + 1):
                clauses += str(-formeInjective(i, j, k)) + " " + str(-formeInjective(i, l, k)) + " 0\n"
    return clauses


def formeInjective(i, j, nbBoxes):
    """
    Fonction pour convertir la paire (i, j) en un littéral unique pour le problème SAT.

    :param i: Indice de la balle
    :param j: Indice de la boîte
    :param nbBoxes: Nombre total de boîtes
    :return: Littéral unique
    """
    if i < 0:
        i = abs(i)
        j = abs(j)
        return -1 * ((nbBoxes * (i - 1)) + j)  # -(i, j) --> -((k*i-1) +j)
    else:
        return (nbBoxes * (i - 1)) + j  # (i, j) --> (k*i-1) +j


def formeInjective_inverse(x, nbBoxes):
    """
    Fonction inverse de formeInjective, convertit le littéral x en la paire (i, j).

    :param x: Littéral
    :param nbBoxes: Nombre total de boîtes
    :return: Paire (i, j)
    """
    if x < 0:
        x = abs(x)
        i = ((x - 1) // nbBoxes) + 1
        j = ((x - 1) % nbBoxes) + 1
        return -i, -j
    else:
        i = ((x - 1) // nbBoxes) + 1
        j = ((x - 1) % nbBoxes) + 1
        return i, j


def genererFichierClauses(k, n, fileName):
    """
    Génère un fichier CNF contenant les clauses d'une instance du problème Schur SAT.

    :param k: Nombre de boîtes
    :param n: Nombre de balles
    :param fileName: Nom du fichier de sortie
    """
    clauses = generate_schur_sat_instance(k, n)
    nombreLitteraux = n * k
    fichier = open(fileName, "w")
    fichier.write("p cnf " + str(nombreLitteraux) + " " + str(len(clauses.splitlines())) + "\n")
    fichier.write(clauses)
    fichier.close()


def show_solution(solutionFileName, k):
    """
    Affiche la solution du problème Schur SAT à partir du fichier retourné par MiniSat.

    :param solutionFileName: Nom du fichier de solution
    :param k: Nombre de boîtes
    """
    with open(solutionFileName, 'r') as f:
        lines = f.readlines()
    if lines[0].strip() == "SAT":
        literals = [int(val) for val in lines[1].split()[:-1]]
        litteraux = [formeInjective_inverse(valuation, k) for valuation in literals if valuation > 0]

        boites = {i: [] for i in range(1, k + 1)}
        for balle, boite in litteraux:
            if boite > 0:
                boites[boite].append(balle)
        show = ""
        for i in range(1, k + 1):
            for boite in boites[i]:
                show += str(boite) + " "
            show += '\n'
        print(show)

    else:
        print("La formule n'est pas satisfaisable.")

# Exemple d'utilisation :
# genererFichierClauses(3, 20, "instances/3_20.cnf")
# show_solution("solutions/3_20.out", 3)
