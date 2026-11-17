notes = [12, 13, 14]

for note in notes:
    print(f"Notes: {note} /20") 

for i in range(1, len(notes)):
    variation = notes[i] - notes[i - 1]
    print(f"Evaluation {i + 1}: variation de {variation:.1f} points")