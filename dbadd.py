alfavit_eng =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_kz = 'АӘБДГҒЕЁЖЗИЙКҚЛМНҢОӨПРСТҰҮФХҺЦЧШЩЪЫІЬЭЮЯАӘБДГҒЕЁЖЗИЙКҚЛМНҢОӨПРСТҰҮФХҺЦЧШЩЪЫІЬЭЮЯ'

l = input("Change RU, KZ or ENG: ").upper()
itog = ''    #создаем переменную для вывода итогового сообщения

if l == "RU":
    message = input("Введите сообщение: ").upper()    #создаем переменнную, куда запишем наше сообщение
    smeshenie = int(13)    #Создаем переменную с шагом шифровки
    for i in message:
        mesto = alfavit_ru.find(i)  
        new_mesto = mesto + smeshenie
        if i in alfavit_ru:
            itog += alfavit_ru[new_mesto]  # Задаем значения в итог
        else:
            itog += i
    
if l == "KZ":
    message = input("Мәтінді енгізіңіз: ").upper()    #создаем переменнную, куда запишем наше сообщение
    smeshenie = int(20)    #Создаем переменную с шагом шифровки
    for i in message:
        mesto = alfavit_kz.find(i)  
        new_mesto = mesto + smeshenie
        if i in alfavit_kz:
            itog += alfavit_kz[new_mesto]  # Задаем значения в итог
        else:
            itog += i

if l == "ENG":
    message = input("Type the text: ").upper()    #создаем переменнную, куда запишем наше сообщение
    smeshenie = int(13)    #Создаем переменную с шагом шифровки
    for i in message:
        mesto = alfavit_eng.find(i)  
        new_mesto = mesto + smeshenie
        if i in alfavit_eng:
            itog += alfavit_eng[new_mesto]  # Задаем значения в итог
        else:
            itog += i

else:
    print("Invalid language. Try again.")

print (itog) 

'''for i in message:
    mesto = alfavit.find(i)  
    new_mesto = mesto + smeshenie
    if i in alfavit:
        itog += alfavit[new_mesto]  # Задаем значения в итог
    else:
        itog += i
print (itog)'''

# symbol.find(i)