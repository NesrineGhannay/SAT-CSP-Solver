import os


def generate_schur_csp_instance(n, k):
    clauses = ""
    # si on a trois balles x, y, z telles que x + y = z, alors les trois balles ne doivent pas toutes êtres dans la même boîte
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for l in range(j + 1, n + 1):
                if (i + j == l):
                    for m in range(1, k + 1):
                        clauses += formeInjective(-i, -m) + " ", formeInjective(-j, -m) + " " + formeInjective(-l, -m) + " 0 \n"

    # Chaque balle est sur au moins dans une case
    for i in range(1, n + 1):
        clause = ""
        for j in range(1, k + 1):
            clause += formeInjective(i, j) + " "
        clauses += clause + "0 \n"

    # Chaque balle est sur au plus dans une case
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(j + 1, k + 1):
                clauses += formeInjective(-i, -j) + " " + formeInjective(-i, -l) + " 0 \n"
    return clauses


def formeInjective(i, j, nbBoxes):
    if i < 0:
        i = abs(i)
        j = abs(j)
        return  (-1 * (nbBoxes * (i - 1) + j))   # -(i, j) --> -(k*i-1 +j)
    else:
        return (nbBoxes * (i - 1) + j)  # (i, j) --> k*i-1 +j


