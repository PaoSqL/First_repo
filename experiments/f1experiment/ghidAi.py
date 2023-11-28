# text editor si ai.consultant pentru aplicatie interogare si ghidare client turist
intro_client = input (f'Salutare, mă numesc Iaphet și sunt consultantul tău turistic'
                    f' în minunata ta excursie prin deșertul Giza,'
                    f' cu cine am onoarea în această deosebită călătorie? - ')  # user is introducing to his name

# raspuns client
def client_trigger():
    print(f'Ne bucuram sa auzim ca aveti o experienta placuta in compania noastra!')
    input(f'altceva')

# raspuns la trigger f de cuvinte cheie
def procesare_raspuns(raspuns_utilizator, cuvinte_cheie):
    for cuvant_cheie in cuvinte_cheie:
        if cuvant_cheie in raspuns_utilizator:
            client_trigger()
            return  # iesi din functie daca ai cel putin un raspuns
    print(f'Mai multe detalii va rog')

# def lista de cuvinte cheie
cuvinte_cheie = ["da", "super", "minunat", "bine"]  # Cuvântul cheie

# raspuns
raspuns_utilizator = print(f'Stimate client {intro_client.upper()} iti pot face experienta acestei calatorii mai placuta fiind asistentul tau de calatorie')
raspuns_utilizator = input(f'Cum a decurs calatoria de azi? - ')

# procesare
procesare_raspuns(raspuns_utilizator, cuvinte_cheie)


# def functie_trigger():
#     print("Funcția a fost activată!")
#
# def procesare_raspuns_utilizator(raspuns_utilizator):
#     cuvant_cheie = "activare"  # Cuvântul cheie pe care îl cauți în răspunsul utilizatorului
#
#     if cuvant_cheie in raspuns_utilizator:
#         functie_trigger()
#     else:
#         print("Cuvântul cheie nu a fost găsit în răspunsul utilizatorului.")
#
# # Primește răspunsul utilizatorului
# raspuns_utilizator = input("Te rog introdu un răspuns: ")
#
# # Procesează răspunsul utilizatorului
# procesare_raspuns_utilizator(raspuns_utilizator)












# def extract_word(input_string):
#     # Split the input string into a list of words
#     words = input_string.split()
#
#     # Assume the word you want is the first one (you can adjust this based on your needs)
#     if words:
#         return words[0]
#     else:
#         return None  # Return None if the input string has no words
#
# def other_function(word):
#     # Use the extracted word in another function
#     print("The extracted word is:", word)
#     # Perform other operations with the word here
#
# # Example usage:
# input_string = "Hello, world! This is a sample string."
# selected_word = extract_word(input_string)
# other_function(selected_word)
