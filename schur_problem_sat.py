import os


def generate_schur_csp_instance(n, k):
    clauses = []

    # si on a trois balles x, y, z telles que x + y = z, alors les trois balles ne doivent pas toutes êtres dans la même boîte
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for l in range(j + 1, n + 1):
                if (i + j == l):
                    for m in range(1, k + 1):
                        clauses.append([(-i, -m), (-j, -m), (-l, -m)])

    # Chaque balle est sur au moins dans une case
    for i in range(1, n + 1):
        clause = []
        for j in range(1, k + 1):
            clause.append((i, j))
        clauses.append(clause)

    # Chaque balle est sur au plus dans une case
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(j + 1, k + 1):
                clauses.append([(-i, -j), (-i, -l)])
    return clauses


def formeInjective(clauses, k):
    nouvellesClauses = []
    for clause in clauses:
        nouvelleClause = []
        for litteral in clause:
            i = litteral[0]
            j = litteral[1]
            if i < 0:
                i = abs(i)
                j = abs(j)
                nouvelleClause.append(-1 * (k * (i - 1) + j))  # -(i, j) --> -(k*i-1 +j)
            else:
                nouvelleClause.append(k * (i - 1) + j)  # (i, j) --> k*i-1 +j
        nouvellesClauses.append(nouvelleClause)
    return nouvellesClauses


print(formeInjective([[(-1, 1), (-2, 1), (-3, 1)]], 3))


def inverseFormeInjective(clausesInjectives, k):
    originalesClauses = []
    for clause in clausesInjectives:
        originaleClause = []
        for litteral in clause:
            if litteral < 0:
                litteral = abs(litteral)
                i = (litteral - 1) // k + 1
                j = (litteral - 1) % k + 1
                originaleClause.append((-i, -j))
            else:
                i = (litteral - 1) // k + 1
                j = (litteral - 1) % k + 1
                originaleClause.append((i, j))
        originalesClauses.append(originaleClause)
    return originalesClauses


c = [[1, 2, 3], [-4, -5, 6]]

# print(inverseFormeInjective(c, 3))
# print(inverseFormeInjective([[-9, -5, -1], [-13, -9, -1]], 4))
#print(inverseFormeInjective([[-1, -4, -7]], 3))

def genererFichierClauses(n, k, fileName):
    clausesTuples = generate_schur_csp_instance(n, k)
    clauses = formeInjective(clausesTuples, k)
    nombreLitteraux = n * k
    fichier = open(fileName, "w")
    fichier.write("cnf " + str(nombreLitteraux) + " " + str(len(clauses)) + "\n")
    for clause in clauses:
        ligne = ""
        for i in range(len(clause) - 1):
            ligne += str(clause[i])
            ligne += " "
        ligne += str(clause[-1])
        ligne += " 0 "
        ligne += "\n"
        fichier.write(ligne)
    fichier.close()


#genererFichierClauses(4, 3, "4balles_3boites.cnf")


def show_solution(solutionFileName):
    f = open(solutionFileName, 'r')
    lines = f.readlines()
    litteraux = []
    for litteral in lines :
        if litteral != 0 :
            litteraux.append(litteral)

    litteraux = inverseFormeInjective()

    resultat = ""

    print(resultat)
