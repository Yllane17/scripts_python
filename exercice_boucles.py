# =================================
# NOMBRE DE NOTES SUPERIEURES À 10
# =================================

notes = [8, 12, 15, 17, 10, 6]
for note in notes :
    if note >= 10  :
        print(f"Les notes superieures à 10 sont: {note} /20")

# =================================
# PARCOURS AVEC UNE BOUCLE
# =================================

for note in notes :
    if note < 10 :
        print(f"ECHEC pour la note : {note}")
    elif note >= 14 :
        print(f"MENTION pour la note : {note}")
    else :
        print(f"PASSABLE pour la note : {note}")


# =================================
# SIMULATION DE LA PROGRESSION
# =================================

score = 40
objectif = 60
progression = 0.03
semaine = 0

while score < objectif :
    score = score * (1+ progression)
    semaine = semaine +1

print(f"Le nombre de semaine qu'il faut est de : {semaine} semaines")

# =================================
# COMBINAISON : FOR ET COMPARAISON
# =================================

notes_examen = [12,15,16,17]
notes_cc = [17,15,12,116]

for note_ex in notes_examen :
    for note_c in notes_cc :
        if note_ex > note_c :
            print("Il y'a PROGRESSION")
        else :
            print("Il n y'a PAS DE PROGRESSION")