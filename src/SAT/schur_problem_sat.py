from collections import defaultdict
import os


def generate_schur_csp_instance(k, n):
    clauses = ""

    # si on a trois balles x, y, z telles que x + y = z, alors les trois balles ne doivent pas toutes être dans la
    # même boîte
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for l in range(j + 1, n + 1):
                if (i + j == l):
                    for m in range(1, k + 1):
                        clauses += str(formeInjective(-i, -m, k)) + " " + str(formeInjective(-j, -m, k)) + " " + str(
                            formeInjective(-l, -m, k)) + " 0\n"

    # Chaque balle est sur au moins dans une case
    for i in range(1, n + 1):
        clause = ""
        for j in range(1, k + 1):
            clause += str(formeInjective(i, j, k)) + " "
        clauses += clause + "0\n"

    # Chaque balle est sur au plus dans une case
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(j + 1, k + 1):
                clauses += str(-formeInjective(i, j, k)) + " " + str(-formeInjective(i, l, k)) + " 0\n"
    return clauses


def formeInjective(i, j, nbBoxes):
    if i < 0:
        i = abs(i)
        j = abs(j)
        return -1 * ((nbBoxes * (i - 1)) + j)  # -(i, j) --> -((k*i-1) +j)
    else:
        return (nbBoxes * (i - 1)) + j  # (i, j) --> (k*i-1) +j


def formeInjective_inverse(x, nbBoxes):
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
    clauses = generate_schur_csp_instance(k, n)
    nombreLitteraux = n * k
    fichier = open(fileName, "w")
    fichier.write("p cnf " + str(nombreLitteraux) + " " + str(len(clauses.splitlines())) + "\n")
    fichier.write(clauses)
    fichier.close()


def show_solution(solutionFileName, k):
    with open(solutionFileName, 'r') as f:
        lines = f.readlines()
    if lines[0].strip() == "SAT":
        literals = [int(val) for val in lines[1].split()[:-1]]
        litteraux = [formeInjective_inverse(valuation, k) for valuation in literals if valuation > 0]

        boites = {i: [] for i in range(1, k + 1)}
        for balle, boite in litteraux:
            if boite > 0:
                boites[boite].append(balle)

        for i in range(1, k + 1):
            print(boites[i])

    else:
        print("La formule n'est pas satisfaisable.")


#genererFichierClauses(3, 100, "3_100.cnf")
show_solution("solutions/3_4.out", 3)