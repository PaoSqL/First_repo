# Flow control - if / else
# evalueaza conditii si bifurca codul  in functie de rezultat

piesa_faina = False
print('pornim radio')
if piesa_faina == True:
    print('dau mai tare muzica')
    print('cant melodia')
print('oprim radio')

# if/else
# daca numarul este par printam acest lucru
# altfel printam impar

nr = -3
# ce inseamna par? se impare exact la 2
# ce  inseamna ca se impare la 2? ne da restul 0

if nr % 3 == 0: # aici se raporteaza rezultatul
    print('nr par')
else:
    print('impar')

# este un numar pozitiv?
if (nr > 0):
    print('pozitiv')
else:
    print('nr nu este pozitiv')

# daca utilizatorul are sub 18 ani nu poate paria, altfel poate

# if, else if, else       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# un robotel care deschide usa si ne saluta la intrarea intr-un hotel
# cum ne saluta robotelul in functie de ora, cu ce text? (Buna ziua sau Buna seara)
# luam date de la tastatura si ne asiguram ca sunt transformate in int
ora = int(input('Introdu ora'))
# print(ora == 17)
if ora < 0:
    print('ora negativa')
   # print('te rugam sa introduci o ora valida') # correct de input from FrontEnd
elif ora <= 11:
    print('Buna dimineata!')
elif ora <= 18:
    print('Buna ziua!')
elif ora <= 21:
    print('Buna seara!')
elif ora <= 24:
    print('Noapte buna!')
else:
    print('ora este mai mare decat 24, te rugam sa introduci o ora valida')
CTRL + / => COMENTEAZA SAU DECOMENTEAZA
robotel telefonic
optiunea = int(input('Alege-ti va rog optiunea dorita!: '))
if optiunea == 0:
    print('Reveniti la meniul anterior')
elif optiunea == 1:
    print('Ati ales limba romana')
elif optiunea == 2:
    print('Ati ales limba engleza')
else:
    print('Nu ati ales o optiune valida, va rugam reveniti la meniul anterior')
