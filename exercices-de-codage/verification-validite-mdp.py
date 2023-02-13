"""
Dans cet exercice, vous devez :

Afficher la phrase mdp_trop_court en majuscule si la longueur du mot de passe entré est égale à 0.

Afficher la phrase mdp_trop_court avec une majuscule sur la première lettre si la longueur du mot de passe entré est plus petite que 8.

Afficher la phrase "Votre mot de passe ne contient que des nombres." si le mot de passe entré ne contient que des nombres.

Afficher la phrase "Inscription terminée." si le mot de passe est valide.

Script de départ :

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
Questions pour cet exercice
Comment utiliser les structures conditionnelles et des méthodes de chaînes de caractères pour vérifier la validité du mot de passe ?
"""

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

if len(mdp) == 0: # La méthode len(mdp) retourne la longueur du mot de passe entré, cette valeur est comparée de 0 et 8 pour vérifier si la longueur est égale à 0 ou plus petite que 8
    print(mdp_trop_court.upper()) # La méthode upper() met toutes les lettres de la chaîne en majuscule
elif len(mdp) < 8: 
    print(mdp_trop_court.capitalize()) # La méthode capitalize() met la première lettre de la chaîne en majuscule et les autres en minuscule
elif mdp.isdigit(): # La méthode isdigit() renvoie True si la chaîne ne contient que des chiffres et False dans le cas contraire
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée")