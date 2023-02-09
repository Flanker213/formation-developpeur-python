"""
001 - Déclarer des variables
Notions abordées : les variables.

On commence simple avec ce premier exercice, qui consiste à déclarer différents types de variables.

La variable 'prenom' qui doit contenir la chaîne de caractère Pierre.
La variable 'age' qui doit contenir le nombre 20.
La variable 'majeur' qui doit contenir un boolean vrai.
La variable 'compte_en_banque' qui doit contenir le nombre décimal 20135,384.
La variable 'amis' qui doit contenir une liste contenant trois chaînes de caractères : Marie, Julien et Adrien.
La variable 'parents' qui doit contenir un tuple contenant deux chaînes de caractères : Marc et Caroline.
"""


prenom = "Pierre" # chaîne de caractère - Une chaîne de caractère doit être entourée de deux guillemets
                  # Pour définir une chaîne de caractère, il faut utiliser le même type de guillemet en ouverture et fermeture.
age = 20 # nombre
majeur = True # boolean - Un booléen commence par une majuscule et peut contenir deux valeurs, True ou False
compte_en_banque = 20135.384 # nombre décimal - Pour définir un nombre décimal, on utilise le point (.) et non pas la virgule
amis = ["Marie","Julien","Adrien"] # liste - Pour définir une liste, on utilise les crochets : [ ]
parents = ("Marc","Caroline") # tuple - Pour définir un tuple, on utilise les parenthèses : ( )

print(prenom)
print(age)
print(majeur)
print(compte_en_banque)
print(amis)
print(parents)