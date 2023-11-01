def file_to_binary(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        binary_content = ''.join(format(byte, '08b') for byte in content)
    return binary_content

def format_binary_letters(binary_content, letter_mapping):
    return ''.join([letter_mapping[binary_content[i:i+8]] for i in range(0, len(binary_content), 8)])

def save_text_to_file(text_content, output_filename):
    with open(output_filename, 'w') as file:
        file.write(text_content)

# Запрос имени файла у пользователя
input_filename = input("Enter file name: ")

# Проверка на существование файла
try:
    with open(input_filename):
        pass
except FileNotFoundError:
    print("File not found.")
    quit()

# Новый letter_mapping
letter_mapping = {
    '00000000': 'aaaa', '00000001': 'aaak', '00000011': 'aaar', '00000010': 'aaap', '00000100': 'aaka', '00000101': 'aakk', '00000111': 'aakr', '00000110': 'aakp', '00001100': 'aara', '00001101': 'aark', '00001111': 'aarr', '00001110': 'aarp', '00001000': 'aapa', '00001001': 'aapk', '00001011': 'aapr', '00001010': 'aapp', '00010000': 'akaa', '00010001': 'akak', '00010011': 'akar', '00010010': 'akap', '00010100': 'akka', '00010101': 'akkk', '00010111': 'akkr', '00010110': 'akkp', '00011100': 'akra', '00011101': 'akrk', '00011111': 'akrr', '00011110': 'akrp', '00011000': 'akpa', '00011001': 'akpk', '00011011': 'akpr', '00011010': 'akpp', '00110000': 'araa', '00110001': 'arak', '00110011': 'arar', '00110010': 'arap', '00110100': 'arka', '00110101': 'arkk', '00110111': 'arkr', '00110110': 'arkp', '00111100': 'arra', '00111101': 'arrk', '00111111': 'arrr', '00111110': 'arrp', '00111000': 'arpa', '00111001': 'arpk', '00111011': 'arpr', '00111010': 'arpp', '00100000': 'apaa', '00100001': 'apak', '00100011': 'apar', '00100010': 'apap', '00100100': 'apka', '00100101': 'apkk', '00100111': 'apkr', '00100110': 'apkp', '00101100': 'apra', '00101101': 'aprk', '00101111': 'aprr', '00101110': 'aprp', '00101000': 'appa', '00101001': 'appk', '00101011': 'appr', '00101010': 'appp', '01000000': 'kaaa', '01000001': 'kaak', '01000011': 'kaar', '01000010': 'kaap', '01000100': 'kaka', '01000101': 'kakk', '01000111': 'kakr', '01000110': 'kakp', '01001100': 'kara', '01001101': 'kark', '01001111': 'karr', '01001110': 'karp', '01001000': 'kapa', '01001001': 'kapk', '01001011': 'kapr', '01001010': 'kapp', '01010000': 'kkaa', '01010001': 'kkak', '01010011': 'kkar', '01010010': 'kkap', '01010100': 'kkka', '01010101': 'kkkk', '01010111': 'kkkr', '01010110': 'kkkp', '01011100': 'kkra', '01011101': 'kkrk', '01011111': 'kkrr', '01011110': 'kkrp', '01011000': 'kkpa', '01011001': 'kkpk', '01011011': 'kkpr', '01011010': 'kkpp', '01110000': 'kraa', '01110001': 'krak', '01110011': 'krar', '01110010': 'krap', '01110100': 'krka', '01110101': 'krkk', '01110111': 'krkr', '01110110': 'krkp', '01111100': 'krra', '01111101': 'krrk', '01111111': 'krrr', '01111110': 'krrp', '01111000': 'krpa', '01111001': 'krpk', '01111011': 'krpr', '01111010': 'krpp', '01100000': 'kpaa', '01100001': 'kpak', '01100011': 'kpar', '01100010': 'kpap', '01100100': 'kpka', '01100101': 'kpkk', '01100111': 'kpkr', '01100110': 'kpkp', '01101100': 'kpra', '01101101': 'kprk', '01101111': 'kprr', '01101110': 'kprp', '01101000': 'kppa', '01101001': 'kppk', '01101011': 'kppr', '01101010': 'kppp', '11000000': 'raaa', '11000001': 'raak', '11000011': 'raar', '11000010': 'raap', '11000100': 'raka', '11000101': 'rakk', '11000111': 'rakr', '11000110': 'rakp', '11001100': 'rara', '11001101': 'rark', '11001111': 'rarr', '11001110': 'rarp', '11001000': 'rapa', '11001001': 'rapk', '11001011': 'rapr', '11001010': 'rapp', '11010000': 'rkaa', '11010001': 'rkak', '11010011': 'rkar', '11010010': 'rkap', '11010100': 'rkka', '11010101': 'rkkk', '11010111': 'rkkr', '11010110': 'rkkp', '11011100': 'rkra', '11011101': 'rkrk', '11011111': 'rkrr', '11011110': 'rkrp', '11011000': 'rkpa', '11011001': 'rkpk', '11011011': 'rkpr', '11011010': 'rkpp', '11110000': 'rraa', '11110001': 'rrak', '11110011': 'rrar', '11110010': 'rrap', '11110100': 'rrka', '11110101': 'rrkk', '11110111': 'rrkr', '11110110': 'rrkp', '11111100': 'rrra', '11111101': 'rrrk', '11111111': 'rrrr', '11111110': 'rrrp', '11111000': 'rrpa', '11111001': 'rrpk', '11111011': 'rrpr', '11111010': 'rrpp', '11100000': 'rpaa', '11100001': 'rpak', '11100011': 'rpar', '11100010': 'rpap', '11100100': 'rpka', '11100101': 'rpkk', '11100111': 'rpkr', '11100110': 'rpkp', '11101100': 'rpra', '11101101': 'rprk', '11101111': 'rprr', '11101110': 'rprp', '11101000': 'rppa', '11101001': 'rppk', '11101011': 'rppr', '11101010': 'rppp', '10000000': 'paaa', '10000001': 'paak', '10000011': 'paar', '10000010': 'paap', '10000100': 'paka', '10000101': 'pakk', '10000111': 'pakr', '10000110': 'pakp', '10001100': 'para', '10001101': 'park', '10001111': 'parr', '10001110': 'parp', '10001000': 'papa', '10001001': 'papk', '10001011': 'papr', '10001010': 'papp', '10010000': 'pkaa', '10010001': 'pkak', '10010011': 'pkar', '10010010': 'pkap', '10010100': 'pkka', '10010101': 'pkkk', '10010111': 'pkkr', '10010110': 'pkkp', '10011100': 'pkra', '10011101': 'pkrk', '10011111': 'pkrr', '10011110': 'pkrp', '10011000': 'pkpa', '10011001': 'pkpk', '10011011': 'pkpr', '10011010': 'pkpp', '10110000': 'praa', '10110001': 'prak', '10110011': 'prar', '10110010': 'prap', '10110100': 'prka', '10110101': 'prkk', '10110111': 'prkr', '10110110': 'prkp', '10111100': 'prra', '10111101': 'prrk', '10111111': 'prrr', '10111110': 'prrp', '10111000': 'prpa', '10111001': 'prpk', '10111011': 'prpr', '10111010': 'prpp', '10100000': 'ppaa', '10100001': 'ppak', '10100011': 'ppar', '10100010': 'ppap', '10100100': 'ppka', '10100101': 'ppkk', '10100111': 'ppkr', '10100110': 'ppkp', '10101100': 'ppra', '10101101': 'pprk', '10101111': 'pprr', '10101110': 'pprp', '10101000': 'pppa', '10101001': 'pppk', '10101011': 'pppr', '10101010': 'pppp'
}
binary_content = file_to_binary(input_filename)
formatted_letters = format_binary_letters(binary_content, letter_mapping)

output_filename = 'output.tk'
save_text_to_file(formatted_letters, output_filename)
print(f"File saved as: {output_filename}.")
