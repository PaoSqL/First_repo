# Listele in python pot sa cuprinda elemente de tipuri diferite

# au dimensiune dinamica
fructe = ['mar', 'banana', 'portocala', 3, True]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print('ultimul element: ', last)
# print(f'lista: ', fructe) varianta 2
print('lista: ', fructe)

# fructe.sort/count/remove/insert/copy/clear etc!! f.method // string.method

# de cate ori apare un element
print(fructe.count(3))

# extindem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)