# ===============================
# AFFICHAGE LISTE
# ===============================

notes = [12, 15, 5, 9, 12.5, 17]

# PREMIERE VALEUR
print(notes[1])

# DERNIERE VELEUR
print(notes[-1])

# 3 PREMIERES VALEURS
print(notes[0:3])

# ===============================
# CALCUL MIN MAX MOY
# ===============================

minimum = min(notes)
maximum = max(notes)
moy_note = sum(notes) /len(notes)

print(f"Le minimum est : {minimum}") 
print(f"Le maximum est : {maximum}")
print(f"La moyenne est : {moy_note}")

# ===============================
# AJOUT ET RETRAIT D'UNE VALEUR
# ===============================

notes.append(16)
notes.pop(0)
print(notes)

# ===============================
# LISTE DE LISTES
# ===============================

etudiants = [
    ["Yllane", 20, 14.5],
    ["Dave", 21, 18.5],
    ["Doni", 18, 17.50],
]

print(etudiants[1][1])

# ===============================
# SOMME DES MOYENNES DE LA LISTE
# ===============================

somme = etudiants[0][2] + etudiants[1][2] + etudiants[2][2]
moy_etudiant = somme / len(etudiants)
print(f"La moyenne des etudiants est de : {moy_etudiant}")

# ===============================
# COPIE DE LA LISTE
# ===============================

etudes = ['Programmation Backend', 'Django']
ajout_etudes = etudes.copy()
ajout_etudes.append("Programmation Frontend")
ajout_etudes.append("Angular")
print(f"Liste des Etudes : {etudes}")
print(f"Liste des Etudes à jour : {ajout_etudes}")