"""
Créer une chaîne de caractères avec une f-string
Dans cet exercice, vous devez recréer l'URL du site https://www.docstring.fr/glossaire/ grâce aux différents variables et à l'aide d'une f-string.

Pour valider l'exercice, la variable URL doit contenir très précisément la chaîne de caractères https://www.docstring.fr/glossaire/ 
(n'oubliez aucun caractère, même pas le slash à la fin).
"""

# Ne modifiez pas les variables ci-dessous
protocole = "https://"
nom_du_site = "docstring"
extension = "fr"
page = "glossaire"

# Modifiez le code à partir d'ici 
URL = f"{protocole}www.{nom_du_site}.{extension}/{page}/"