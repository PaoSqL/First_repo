# aici ne facem obiectele
from oop.cont_bancar import cont_bancar

cont1 = cont_bancar('Andy S', 'R0001')
cont2 = cont_bancar('Crina S', 'R0002')

cont1.activare_cont(3333)
cont1.activare_cont(7777)
cont2.activare_cont(7777)

cont1.interogare_sold()
cont2.interogare_sold()

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plata_card(500)
cont1.plata_card(300)
cont2.plata_card(100)
cont2.plata_card(200)

cont1.interogare_sold()
cont2.interogare_sold()

# tema
# clasa angajat
# nume, prenume, salariu, vechime
# consreuctor : nume, prenume, salariu, functie, vechime
# metode
# descriere
# marire salariu in f de vechime
# actualizare vechime (param noua vechime)
        # self.vechime = noua_vechime
# daca are vechime sub 5 ani, marim cu 300, peste 5 ani, 500