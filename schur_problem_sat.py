import os


def generate_schur_csp_instance(n, k):
    clauses = []

    # si on a trois balles x, y, z telles que x + y = z, alors les trois balles ne doivent pas toutes êtres dans la même boîte
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for l in range(1, n + 1):
                for m in range(1, k + 1):
                    if (i + j == l) and (i != j != l):
                        clauses.append([(-i, -m), (-j, -m), (-l, -m)])


    # chaque balle est sur au moins dans une case
    for i in range(1, n + 1):
        clause = []
        for j in range(1, n + 1):
            clause.append((i, j))
        clauses.append(clause)

    # Chaque balle est sur au plus
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(1, k + 1):
                if j != l:
                    clauses.append([(-i, -j), (-i, -l)])
    return clauses


# print(generate_schur_csp_instance(4, 3))


def formeInjective(clauses, n):
    nouvellesClauses = []
    for clause in clauses:
        nouvelleClause = []
        for litteral in clause:
            i = litteral[0]
            j = litteral[1]
            if i < 0:
                i = abs(i)
                j = abs(j)
                nouvelleClause.append(-1 * (n * (i - 1) + j))  # -(i, j) --> -(n*i-1 +j)
            else:
                nouvelleClause.append(n * (i - 1) + j)  # (i, j) --> n*i-1 +j
        nouvellesClauses.append(nouvelleClause)
    for clause in nouvellesClauses:
        clause.sort()
    clausesSansDoubles = []
    [clausesSansDoubles.append(clause) for clause in nouvellesClauses if clause not in clausesSansDoubles]
    return clausesSansDoubles


def countNbLiterals(clauses):
    """
    Compte le nombre total de littéraux uniques dans une liste de clauses.
    Un littéral est représenté sous forme de tuple (a, b).
    """
    unique_literals = set()

    for clause in clauses:
        for literal in clause:
            unique_literals.add(literal)
    return len(unique_literals)

#print(countNbLiterals([[(-1, -1), (-2, -1), (-3, -1)], [(-5, -1), (-2, -4), (-8, -1)]]))

def genererFichierClauses(n, k, fileName):
    clausesTuples = generate_schur_csp_instance(n, k)
    clauses = formeInjective(clausesTuples, n)
    nombreLitteraux = countNbLiterals(clausesTuples)
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

genererFichierClauses(4, 3, "4balles_3boites.cnf")