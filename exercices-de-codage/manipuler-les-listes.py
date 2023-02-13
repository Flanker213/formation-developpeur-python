"""
Manipuler des listes
Dans cet exercice, vous allez devoir manipuler plusieurs listes :

Récupérez le premier et le dernier nombre contenus dans cette liste dans les variables 'nombre_premier' et 'nombre_dernier'.

nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = 
nombre_dernier = 
Récupérer l'élément 'Python' contenu dans la liste dans la variable 'langage'.

langages = ["Java", "Python", "C++"]
langage = 
Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])

liste = ["Java", "Python", "C++"]
"""

"""
# Récupérez le premier et le dernier nombre contenus dans cette liste dans les variables 'nombre_premier' et 'nombre_dernier'.
nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = 
nombre_dernier = 

# Récupérer l'élément 'Python' contenu dans la liste dans la variable 'langage'.
langages = ["Java", "Python", "C++"]
langage = 

# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])
liste = ["Java", "Python", "C++"]
"""

# Récupérez le premier et le dernier nombre contenus dans cette liste dans les variables 'nombre_premier' et 'nombre_dernier'.
nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = nombres[0] # Je récupère le premier élément de la liste avec l'index 0 qui représente le premier élément de la liste
nombre_dernier = nombres[-1] # Je récupère le dernier élément de la liste avec l'index -1 qui représente le dernier élément nombre

# Récupérer l'élément 'Python' contenu dans la liste dans la variable 'langage'.
langages = ["Java", "Python", "C++"]
langage = langages[1] # Comment "Python" est le deuxième élément dans la liste, j'utilise l'index 1 pour le récupérer

# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])
liste = ["Java", "Python", "C++"]
liste.remove("Python") # J'utilise la methode remove() pour supprimer un élément spécifique de la liste de sa position actuelle
liste.append("Python") # Et j'utilise la methode append() pour l'ajouter à la fin de la liste