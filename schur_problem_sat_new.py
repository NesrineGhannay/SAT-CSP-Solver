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
                print("clause : - (i: ", i, " j: ", j, ") ou -(i: ", i, " l:", l, ")")
                clauses += str(-formeInjective(i, j, k)) + " " + str(-formeInjective(i, l, k)) + " 0\n"
    return clauses


def formeInjective(i, j, nbBoxes):
    if i < 0:
        i = abs(i)
        j = abs(j)
        return -1 * ((nbBoxes * (i - 1)) + j)  # -(i, j) --> -((k*i-1) +j)
    else:
        return (nbBoxes * (i - 1)) + j  # (i, j) --> (k*i-1) +j

print("Forme Injective de 7, 1 : ", formeInjective(7, 1, 3))
print("Forme Injective de 7, 2 : ",formeInjective(7, 2, 3))
print("Forme Injective de 7, 3 : ",formeInjective(7, 3, 3))

"""
def formeInjective_inverse(x, nbBoxes):
    if x < 0:
        x = abs(x)
        j = (x % nbBoxes) + 1
        i = ((x - j - 1) // nbBoxes) + 1
        return -i, -j
    else:
        j = (x % nbBoxes) + 1
        i = ((x - j - 1) // nbBoxes) + 1
        print("x : ", x, " et i, j : ", i, " , ", j)
        return i, j
"""


def formeInjective_inverse(x, nbBoxes):
    if x < 0:
        x = abs(x)
        j = (x % nbBoxes) + 1
        i = ((x - j - 1) // nbBoxes) + 1
        return -i, -j
    else:
        i = ((x - 1) // nbBoxes) + 1
        j = ((x - 1) % nbBoxes) + 1
        print("x : ", x, " et i, j : ", i, " , ", j)
        return i, j



"""
i = (x // nbBoxes) + 1
j = x - ((i - 1) * nbBoxes)"""
"""
print("Reciproque 21 : ", formeInjective_inverse(21, 3))
print("Reciproque 22 : ", formeInjective_inverse(22, 3))
print("Reciproque 27 : ", formeInjective_inverse(27, 3))
print("Reciproque 29 : ", formeInjective_inverse(29, 3))

print("Reciproque -19 : ", formeInjective_inverse(-19, 3))
print("Reciproque -20 : ", formeInjective_inverse(-20, 3))
print("Reciproque 21 : ", formeInjective_inverse(21, 3))"""

"""
print(formeInjective(-456, -10, 15))
print(formeInjective_inverse(-6835, 15))
print(formeInjective(8, 0, 3))
print(formeInjective(8, 1, 3))
"""
"""
print(formeInjective_inverse(2, 3))
print(formeInjective_inverse(4, 3))
print(formeInjective_inverse(7, 3))
print(formeInjective_inverse(10, 3))"""


def genererFichierClauses(k, n, fileName):
    clauses = generate_schur_csp_instance(k, n)
    nombreLitteraux = n * k
    fichier = open(fileName, "w")
    fichier.write("p cnf " + str(nombreLitteraux) + " " + str(len(clauses.splitlines())) + "\n")
    fichier.write(clauses)
    fichier.close()


#genererFichierClauses(3, 20, "instances/3_20.cnf")


def show_solution(solutionFileName, k):
    with open(solutionFileName, 'r') as f:
        lines = f.readlines()
    if lines[0].strip() == "SAT":
        literals = [int(val) for val in lines[1].split()[:-1]]
        #print(" x : ", literals)
        litteraux = [formeInjective_inverse(valuation, k) for valuation in literals if valuation > 0]
        #print("i , j : ", litteraux)

        boites = {i: [] for i in range(1, k + 1)}
        c = 0
        for balle, boite in litteraux:
            # print(litteraux)
            if boite > 0:
                boites[boite].append(balle)
                c += 1

        for i in range(1, k + 1):
            print("Boîte {}: {}".format(i, boites[i]))
        print("Nombre d'affectations : " + str(c))

    else:
        print("La formule n'est pas satisfaisable.")


show_solution("solutions/3_4.out", 3)
# problème :
"""
x :  21  et i, j :  8  ,  0
x :  22  et i, j :  8  ,  1
x :  27  et i, j :  10  ,  0
x :  29  et i, j :  10  ,  2
"""
#(8, 0), (8, 1), (10, 0), (10, 2)