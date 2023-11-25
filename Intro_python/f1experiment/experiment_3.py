def functie_enigmatica(lista):
    return[x for x in lista if x%2==0]
lista_initiala=[1,2,3,4,5,6,7,8,9,10]
rezultat = functie_enigmatica(lista_initiala[:5])+functie_enigmatica(lista_initiala[5:])
print(len(rezultat))