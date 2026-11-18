# ===============================
# DICTIONNAIRE
# ===============================

etudiant = {
    "nom" : "Yllane",
    "age" : 20,
    "filiere" : "CDWFS",
    "moyenne" : 16.5
}

print(f"Informations de l'étudiant" )
print(f"Nom : {etudiant['nom']}")
print(f"Age : {etudiant['age']}")
print(f"Filière : {etudiant['filiere']}")
print(f"Moyenne Générale : {etudiant['moyenne']}")


# ===============================
# CALCUL MOYENNE AVEC DICT
# ===============================

liste = [
    {
        "nom" : "Flenory",
        "note_cc" : 15,
        "note_examen" : 13
    },
    {
        "nom" : "Tariq",
        "note_cc" : 11,
        "note_examen" : 11
    },
    {
        "nom" : "Tee",
        "note_cc" : 18,
        "note_examen" : 10
    }
]
total_moyenne = 0

for etudiants in liste :
    moy_etudiant = etudiants['note_cc']*0.4 + etudiants['note_examen']*0.6
    etudiants['moyenne'] = moy_etudiant
    total_moyenne += moy_etudiant
    print(f"La moyenne de l'etudiant {etudiants['nom']} est de : {moy_etudiant:.2f}")

moy_classe = total_moyenne / len(liste)
print(f"La moyenne générale de la classe est de : {moy_classe:.2f}")


# ===============================
# TUPLE ET AFFICHAGE DE L'ECART
# ===============================

note = (10, 15, 12.5)
note_ii = (13, 17, 15)
note_iii = (12, 14, 13)

print(f"L'écart du tuple 1 est de {note[1]-note[0]}")
print(f"L'écarte du tuple 2 est de {note_ii[1] - note_ii[0]}")
print(f"l'écart du tuple 3 est de {note_iii[1] - note_iii[0]}")

# ===============================
# FONCTION GET()
# ===============================

mention = etudiant.get("Mention", "Elle n'existe pas")
print(f"Y a t-il la mention ? {mention} ")