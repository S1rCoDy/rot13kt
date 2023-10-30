import os

def сжать_данные(data):
    compressed_data = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            if count > 1:
                compressed_data.extend([str(data[i-1]), str(count)])
            else:
                compressed_data.append(str(data[i-1]))
            count = 1

    if count > 1:
        compressed_data.extend([str(data[-1]), str(count)])
    else:
        compressed_data.append(str(data[-1]))

    return ''.join(compressed_data)

def разжать_данные(data):
    decompressed_data = []
    i = 0

    while i < len(data):
        decompressed_data.append(data[i])
        i += 1
        if i < len(data):
            count = int(data[i])
            i += 1
            for _ in range(count - 1):
                decompressed_data.append(data[i-2])

    return ''.join(decompressed_data)

def сжать_файл(путь, место_сохранения):
    with open(путь, 'r') as файл:
        оригинальные_данные = файл.read()
        сжатые_данные = сжать_данные(оригинальные_данные)
        
        сжатый_путь = место_сохранения + ".tk"
        with open(сжатый_путь, 'w') as сжатый_файл:
            сжатый_файл.write(сжатые_данные)
        
        return сжатый_путь

def разжать_файл(путь, место_сохранения):
    with open(путь, 'r') as файл:
        сжатые_данные = файл.read()
        разжатые_данные = разжать_данные(сжатые_данные)
        
        разжатый_путь = место_сохранения + "_разжатый.txt"
        with open(разжатый_путь, 'w') as разжатый_файл:
            разжатый_файл.write(разжатые_данные)
        
        return разжатый_путь

# Выбор файла
путь = input("Введите путь к файлу для сжатия: ")

# Проверяем, существует ли файл
if os.path.exists(путь):
    # Запрашиваем место сохранения
    место_сохранения = input("Введите место сохранения сжатого файла (без расширения): ")
    
    # Проверяем, существует ли папка для сохранения
    if not os.path.exists(место_сохранения):
        os.makedirs(место_сохранения)

    # Спрашиваем у пользователя, что он хочет сделать
    действие = input("Что вы хотите сделать? (сжать/разжать): ")

    if действие == "сжать":
        сжатый_путь = сжать_файл(путь, место_сохранения)
        print(f"Файл сжат и сохранен в {сжатый_путь}")
    elif действие == "разжать":
        разжатый_путь = разжать_файл(путь, место_сохранения)
        print(f"Файл разжат и сохранен в {разжатый_путь}")
    else:
        print("Некорректное действие. Пожалуйста, введите 'сжать' или 'разжать'.")
else:
    print("Файл не существует.")