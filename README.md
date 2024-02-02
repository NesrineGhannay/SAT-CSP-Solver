*@author : GHANNAY Nesrine*

# Modélisation et Résolution par SAT et CSP : Le problème de Schur

## Description
Ce projet explore la modélisation et la résolution informatique du problème de Schur, qui implique la répartition de n balles étiquetées de 1 à n dans k boîtes (avec k ≥ 3). L'objectif est de garantir que pour toute combinaison de trois balles numérotées x, y, z ; si  x + y = z, alors ces trois balles ne peuvent pas être contenues dans une même boîte. Pour aborder cette problématique, nous étudierons deux approches de résolution : SAT (Satisfiability) et CSP (Constraint Satisfaction Problem).

## Dossiers et Fichiers

### SAT
Le dossier SAT contient le code source et les résultats liés à l'approche SAT.

- **Code Source (Python) :** [src/SAT/schur_problem_sat.py](src/SAT/schur_problem_sat.py)
  - Ce fichier contient le code Python pour la modélisation et la résolution du problème de Schur en utilisant la logique propositionnelle (SAT) avec le solveur Minisat.

- **Dossier Instances :** [src/SAT/instances](src/SAT/instances)
  - Ce dossier contient les instances générées du problème de Schur pour l'approche SAT.

- **Dossier Solutions :** [src/SAT/solutions](src/SAT/solutions)
  - Ce dossier contient les solutions générées par le solveur MiniSat pour les instances du problème de Schur.

- **Résultats :** [src/SAT/resultats.txt](src/SAT/resultats.txt)
  - Ce fichier contient les informations de résolution obtenue lors de l'exécution de MiniSat. 

### CSP
Le dossier CSP contient le code source lié à l'approche CSP.

- **Code Source (Python) :** [src/CSP/schur_problem_csp.py](src/CSP/schur_problem_csp.py)
  - Ce fichier contient le code Python pour la modélisation et la résolution du problème de Schur en utilisant les contraintes (CSP) avec la bibliothèque PyCSP3.

## Utilisation

1. **Approche SAT :**
   - Exécutez le fichier [schur_problem_sat.py](src/SAT/schur_problem_sat.py) pour modéliser le problème de Schur en utilisant la logique propositionnelle. Il faudra appeler la fonction **genererFichierClauses**, en précisant le nombre de boîtes **n**, de balles **k** ainsi que le nom que portera votre fichier en sortie. 
   - Utiliser le solveur MiniSAT sur le fichier produit précédemment (n_k.cnf) qui produira un fichier (n_k.out) indiquant la solution trouvée. 
   - Dans le cas où le problème a bien été résolu "SATISFAISABLE" par Minisat, vous pourrez utiliser la seconde fonction **show_solution** comme indiqué dans [schur_problem_sat.py](src/SAT/schur_problem_sat.py) sur le fichier retourné par MiniSat afin d'observer la solution trouvée.
   - Le contenu de chaque boîte sera affiché dans la console.

2. **Approche CSP :**
   - Exécutez le fichier [schur_problem_csp.py](src/CSP/schur_problem_csp.py) pour modéliser et résoudre le problème de Schur en utilisant les contraintes. Il faudra renseigner les bonnes valeurs pour le nombre de boites et de balles. Enfin, n'oubliez pas de préciser le solveur que vous voulez utiliser dans les paramètres de la fonction **solve()** appelée (ACE par défaut, ou CHOCO si renseigné)
   - Les résultats seront affichés dans la console.


