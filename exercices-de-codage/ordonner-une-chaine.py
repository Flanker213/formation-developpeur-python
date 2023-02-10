"""
Ordonner une chaîne de caractères
Cet exercice est assez difficile compte tenu du fait que l'on n'a pas encore vu les listes en détail.

Le but de cet exercice et de remettre en ordre alphabétique les prénoms présents dans la chaîne de caractères.

Vous devez créer une variable chaine_en_ordre qui, à la fin de l'exercice, doit contenir la chaîne de caractères suivante :

Anne, Julien, Lucien, Marie, Pierre

Pour trier une liste, on utilise la méthode sort. On peut aussi utiliser la fonction sorted.

Ces fonctions sont vues avec beaucoup plus de détail dans la suite de la formation, en attendant, voici un petit exemple de la façon dont vous pouvez les utiliser.

- 1. Avec la méthode sort :

>>> liste = [4, 2, 3, 5, 1]
>>> liste.sort()  # La méthode sort modifie directement la liste !
>>> print(liste)
[1, 2, 3, 4, 5]
- 2. Avec la fonction sorted :

>>> liste = [4, 2, 3, 5, 1]
>>> liste = sorted(liste)  # La fonction sorted ne modifie pas directement la liste !
>>> print(liste)
[1, 2, 3, 4, 5]
Comme vous pouvez le voir ci-dessus, la méthode sort modifie directement la liste, pas besoin donc de faire liste = liste.sort().

Ce n'est pas le cas de la fonction sorted qui retourne la liste triée mais ne modifie pas directement la liste en mémoire. Dans ce 2e cas de figure, 
il faut donc affecter le résultat à la variable d'origine : liste = sorted(liste).



Pour le reste de l'exercice, vous devrez utiliser la méthode split et la méthode join que l'on a vu dans ce chapitre.



N'allez pas chercher trop complexe, la solution peut tenir en 3 lignes (mais ce n'est pas grave si vous avez besoin d'un peu plus bien sûr !).



Veillez à bien respecter les virgules et les espaces entre les noms pour valider l'exercice.



Encore une fois, c'est un exercice assez challengeant, n'hésitez pas à faire beaucoup de tests dans Visual Studio Code, à lire la documentation ou à faire des recherches ! 
Et si vous n'y arrivez pas, nul besoin de s'acharner, c'est normal, l'exercice fait appel à beaucoup de notions.
"""

chaine = "Pierre, Julien, Anne, Marie, Lucien"

chaine_liste = chaine.split(", ") # split() Sépare la chaîne de caractères sur les caractères passés en argument et retourne une liste
chaine_liste.sort() # list.sort() modifie les listes
chaine_en_ordre = ", ".join(chaine_liste) # join() Joins avec le caractère spécifié tous les éléments d'un itérable passé en argument