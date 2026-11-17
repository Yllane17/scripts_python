# ============================
# MOYENNE PONDEREE
# ============================

note_cc = 12
note_examen = 15
coef_examen = 0.6

moyenne = note_cc * (1- coef_examen) + note_examen * coef_examen
print(f"votre moyenne est de : {moyenne}")

# ============================
# MOYENNE CLASSE ET ECART
# ============================

nb_copie = 15
total_notes = 187.5

moy_classe = total_notes/nb_copie
ecart = moy_classe - 10
print(f"La moyenne de la classe est : {moy_classe} et son ecart est de: {ecart}")

# ============================
# CONVERTISSEUR DE TYPE
# ============================

note_str = "16.75"
note_str = float(note_str) * 3
print(note_str)

# ============================
# MEILLEUR NOTE MIN MAX
# ============================

note_etudiant1 = 15.10
note_etudiant2 = 15.04
print(f"Le maximum est : {max(note_etudiant1, note_etudiant2)}")