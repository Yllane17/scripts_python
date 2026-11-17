# ====================================
#   CLASSE SANS ATTRIBUTS ET METHODES
# ====================================

# class Etudiant:
#     pass 

# e1 = Etudiant()
# e2 = Etudiant()

# ====================================
#   CLASSE AVEC ATTRIBUTS ET METHODES
# ====================================

class Etudiant:
    def __init__(self, nom, age, filiere):
        self.nom = nom
        self.age = age
        self.filiere = filiere

amina = Etudiant("Amina", 20 , "Genie Logiciel")
brice = Etudiant("Brice", 22, "Reseaux")

print(f"{amina.nom}, {amina.age} ans,{amina.filiere}")
print(f"{brice.nom}, {brice.age} ans, {brice.filiere}")