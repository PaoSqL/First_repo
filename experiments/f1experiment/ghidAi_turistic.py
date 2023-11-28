# text editor si ai.consultant pentru aplicatie interogare si ghidare client turist

interogare_nume_client = input (f'Salutare, mă numesc Iaphet și sunt consultantul tău turistic în minunata ta excursie prin deșertul Giza, cu cine am onoarea în această deosebită călătorie? - ')

# daca clientul isi scrie numele gresit sau cu litere mici, corectam
interogare_nume_clientUp = interogare_nume_client.upper()
rep_client = input(f'Bună ziua {interogare_nume_clientUp}, a fost placuta si lipsita de incidente excursia dvs prin deșertul Giza? - ')

# rescriem raspunsul clientului pentru a fi siguri ca functia recunoaste textul case_sensitive
rep_clientUp = rep_client.upper()
if rep_clientUp == 'DA':
    print(f'Ne bucuram sa auzim ca ati avut o experienta deosebita azi prin desertul Giza.')
elif rep_clientUp == 'NU':
    input(f'Cum ne putem revansa fata de dvs in urmatoarea zi a excursiei? - ')
    print(f'Vom programa pentru maine reluarea experientei dvs de azi si ne pare rau sa auzim ca experienta dvs prin desertul Giza a avut de suferit.')
else:
    print(f'Cu ce putem imbunatati?')
input(f'Doriti sa mai adaugati ceva?')
if input() == 'nu':
    print(f'Atunci pentru alta zi')
else:
    print('f Ne bucaram pentru intelegere')






# if rep_client ==
#     ;
# else:
#     print(f'Ne pare rau');
#
#
# feedback_client = input(f'')


# print(parera_dvsUP)
#
# camile = input("câte cămile ați văzut?"+"")
# camile_user = int(camile)
# camile2 = input("dar dvs câte cămile ați văzut?")
# camile_user2 = int(camile2)
# total2 = total1.upper()
# total = total2 + "am văzut în total" + str(camile_user + camile_user2) + " cămile în deșertul Giza."
# total3 = total.upper()
#
# print(total3)