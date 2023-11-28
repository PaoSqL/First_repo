# robotel ajutor vreme

temp_celsius = 30
umiditate = 10

# if temp_celsius <= 100:
#     print("Esti fiert!!")
# if temp_celsius <= 50:
#     print("Esti copt!!")
# if temp_celsius <= 10:
#     print("Este foarte cald!!")
# if temp_celsius < 0:
#     print("Esti inghetat!!")

if temp_celsius > 50 or umiditate >= 40:
    print('Adevarat')
elif temp_celsius >= 20:
    print('Alta varianta')
    if temp_celsius == 50:
        print('temp mai mica sau egala cu 50')
    else:
        int(input(' dada '))
elif umiditate <= 40:
    print('ploua')
else:
    print('eroare')