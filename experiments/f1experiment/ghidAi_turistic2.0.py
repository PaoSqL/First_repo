# text editor si ai.consultant pentru aplicatie interogare si ghidare client turist

interogare_nume_client = input (f'Salutare, mă numesc Iaphet și sunt consultantul tău turistic'
                                f' în minunata ta excursie prin deșertul Giza,'
                                f' cu cine am onoarea în această deosebită călătorie? - ')  # user is introducing to his name

# daca clientul isi scrie numele gresit sau cu litere mici, corectam
interogare_nume_clientUp = interogare_nume_client.title()

print(f'Stimate client {interogare_nume_clientUp} iti pot face experienta acestei calatorii mai placuta raspunzandu-mi cu da sau nu la urmatoarele intrebari:')

rep_client = input(f'A fost placuta si lipsita de incidente excursia dvs prin deșertul Giza? - ')

# definim trigger "string" pentru a directiona user-ul catre raspunsul pe care il cauta
def feed_positive():
    print(f'Ne bucuram')
def feed_negative():
    print(f'Ne pare rau')
def positive_answer(interogare_nume_clientUp):
    positive = 'DA'
def negative_answer(interogare_nume_clientUp):
    negative = 'NU'

# if rep_clientUp =='DA':
#     print(interogare_nume_clientUp)

# rescriem raspunsul clientului pentru a fi siguri ca functia recunoaste textul case_sensitive
rep_clientUp = rep_client.upper()
if rep_clientUp == 'DA':
    print(f'Ne bucuram sa auzim ca ati avut o experienta deosebita azi prin desertul Giza')
    if rep_satisf = feedback_poss
elif rep_clientUp == 'NU':
    input(f'Va rugam sa ne descrieti ce s-a intamplat: - ')
    if rep_satisf = feedback_neg
elif rep_clientUp == 'lovit':
    user = input(f'Este grav?')
else:
    print(f'Voi transmite mai departe aceste informatii echipei de organizare pentru a ne asigura ca totul va decurge perfect de acum inainte.')
    input(f'Avem mai')


#     print(f'Vom programa pentru maine reluarea experientei dvs de azi si ne pare rau sa auzim ca experienta dvs prin desertul Giza a avut de suferit.')
# else:
#     print(f'Cu ce putem imbunatati?')
# input(f'Doriti sa mai adaugati ceva?')
# if input() == 'nu':
#     print(f'Atunci pentru alta zi')
# else:
#     print('f Ne bucaram pentru intelegere')