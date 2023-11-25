lista_goala = []
map_gol = {}

# declaram si initializam un dict (dictionary)
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}
print(note_elevi)

# adaugam elemente
note_elevi['Sebi'] = 7

# printam dictul
print(note_elevi)

# aflam notele (valorile incapsulate)
print(note_elevi['Gigel'])  # prima varianta
print(note_elevi.get('Gigel'))  # a doua varianta

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# stergem valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu mai este in clasa'))
print(note_elevi)

# returneaza doar cheile - keys ( util: inspect cand vine din input)
print(note_elevi.keys())