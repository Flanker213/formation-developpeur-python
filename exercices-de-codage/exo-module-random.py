"""
Dans cet exercice, vous devez générer deux nombres aléatoires et indiquer à l'utilisateur lequel des deux nombres est le plus grand.

Par exemple :

Un nombre a est généré aléatoirement et prend la valeur de 15.

Un nombre b est généré aléatoirement et prend la valeur de 26.

Votre script doit afficher la phrase suivante :

"Le nombre b est plus grand que le nombre a."

Dans le cas contraire, le script devra afficher :

"Le nombre a est plus grand que le nombre b."

Si les nombres sont égaux, le script devra afficher :

"Le nombre a et le nombre b sont égaux."



Les deux nombres générés aléatoirement peuvent être des nombres entier ou des nombres décimaux, cela n'a pas d'importance. 
Vous pouvez également choisir n'importe quel intervalle pour générer votre nombre aléatoire.
"""

import random

# On commence par générer deux nombres aléatoires avec le module random et la fonction randint
a = random.randint(1,50)
b = random.randint(1,50)

# On utilise ensuite une structure conditionnelle
if a < b:
    print("Le nombre b est plus grand que le nombre a.")
elif a > b:
    print("Le nombre a est plus grand que le nombre b.")
else:
    print("Le nombre a et le nombre b sont égaux.")