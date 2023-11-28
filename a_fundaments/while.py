# problema: masina merge atata timp cat ea are benzina
litri_benzina = 10
while litri_benzina > 0:
    # acceleram
    print("Acceleratie: ON!")
    # scadem benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3:
        print("Se aprinde becul rosu: Va rugam sa realimentati autovehiculul!")
print("STOP! Autovehiculul nu mai are benzina")