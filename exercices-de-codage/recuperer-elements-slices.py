"""
Récupérer des éléments avec les slices
Dans cet exercice, vous devez récupérer différents morceaux d'une liste grâce aux slices.

La liste de départ est la suivante :

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
L'objectif de cet exercice est de récupérer les informations suivantes grâce aux slices :

Les trois premiers employés ("Maxime", "Martine" et "Christopher") dans une liste trois_premiers

Les trois derniers employés ("Carlos", "Michael" et "Éric") dans une liste trois_derniers

Tous les employés sauf le premier et le dernier dans une liste milieu

Le premier et le dernier employé dans une liste premier_dernier
"""

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[0:4]
trois_derniers = liste[3:]
milieu = liste[1:-1]
premier_dernier = liste[::5]

"""
print(liste)
print(trois_premiers)
print(trois_derniers)
print(milieu)
print(premier_dernier)
"""