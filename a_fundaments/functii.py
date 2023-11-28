def print_greetings():
    print('Buna ziua! Bine ati venit!')
def print_greetings_by_name(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def media_numerelor(a, b, c):
    return (a + b + c) / 3  # return este ultimul lucru care se intampla intr-o functie, dupa executarea lui se inchide automat programul
    print('abc')  # acest prin nu se poate printa

def pi_value():
    return 3.14

# exercitiu
# daca nr este pozitiv returnati True, altfel False
# daca persoana este majora
def verificare_major(varsta):
    if varsta >= 18:
        return True
    else:
        return False

# zona de apelare (desktop)
print_greetings()
print_greetings()

print_greetings_by_name('Sinpetrean', 'Andy')
print_greetings_by_name('Marcel', 'Ion')
print_greetings_by_name('Fuego', 'Tudor')
print_greetings_by_name('Razvan', 'Petrean')

media_numerelor(3, 3, 4)
print(media_numerelor(3, 3, 4))

print(pi_value())

print(verificare_major(18))

# exemplu aplicatie de verificare varsta major
# se ia varsta utilizatorului
age = int(input('Introduceti varsta dumneavoastra: '))
if verificare_major(age):
    print('Cont creat. Bine ai venit!')
else:
    print('Nu ai varsta necesara (18) pentru a face cont')

# object_pro - programarea pe obiecte , object oriented programming
# variabile => atribute, proprietati sau fields
# functii => metode