def rot13(text, direction=1):
    result = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            index = symbols.find(char.lower())
            
            # Применяем шифр ROT13 в зависимости от направления (шифровка или расшифровка)
            new_index = (index + direction * 13) % len(symbols)
            
            result += symbols[new_index].upper() if is_upper else symbols[new_index]
        else:
            result += char
    return result

# Ваш алфавит
symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяbdfghijklmnpqrstuvwxyzәғқңөұүАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯBDFGHIJKLMNPQRSTUVWXYZӘҒҚҢӨҰҮ"

# Функция для шифровки текста
def encrypt(text):
    return rot13(text, direction=1)

# Функция для расшифровки текста
def decrypt(text):
    return rot13(text, direction=-1)

zadacha = 

# Пример использования
text = input("Введите текст: ")
print("Исходный текст:", text)

encrypted_text = encrypt(text)
print("Зашифрованный текст:", encrypted_text)

decrypt_text = decrypt(encrypted_text)
print("Расшифрованный текст: ", decrypt_text)
