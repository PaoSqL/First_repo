class cont_bancar:
    # zona de atribute definite prin constructor

    def __init__(self, titular_cont, iban):
        # atribute, variabile, fields
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    def interogare_sold(self):
        print(f'Titular {self.titular_cont}')
        print(f'IBAN {self.iban}')
        print(f'SOLD {self.sold}')
        print(f'Activare cont: {self.activ}')
        print(f'Numar de incercari {self.incercari_activare}')
        print('--------------------------------------------')

    def salut(self):
        print(f'Buna {self.titular_cont}')

    def activare_cont(self, pin_utilizator):
        #print(f'Buna {self.titular_cont}')
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat ')
            self.activ = True
            print('--------------------------------------------')

        else:
            print('Pin gresit')
            self.incercari_activare = self.incercari_activare + 1
            print('--------------------------------------------')
            #self.incercari_activare+=1 , alta modalitate

    def alimentareCont(self, suma):
        #print(f'Buna {self.titular_cont}')
        self.salut()
        self.sold += suma
        print(f'Ati alimentat suma {suma}')
        print(f'Aveti in cont {self.sold}')
        print('--------------------------------------------')


    def plata_card(self, suma):
        # variable scope
        #print(f'Buna {self.titular_cont}')
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
            print('--------------------------------------------')

        else:
            print('Fonduri insuficiente')
            print('--------------------------------------------')

    # nu se poate crea o metoda intr-o alta metoda, dar se poate APELA! o metoda intr-o alta metoda