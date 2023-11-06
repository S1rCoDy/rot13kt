import heapq
import os
import pickle

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    frequency_table = {}
    for char in text:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    return frequency_table

def build_huffman_tree(frequency_table):
    priority_queue = [Node(char, freq) for char, freq in frequency_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        merged_node = Node(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_encoding_table(node, current_code="", encoding_table={}):
    if node is not None:
        if node.char is not None:
            encoding_table[node.char] = current_code
        build_encoding_table(node.left, current_code + "0", encoding_table)
        build_encoding_table(node.right, current_code + "1", encoding_table)
    return encoding_table

def compress_file(file_path, output_path):
    with open(file_path, 'rb') as file:
        text = file.read()

    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)

    compressed_text = ''.join([encoding_table[char] for char in text])
    compressed_bytes = int(compressed_text, 2).to_bytes((len(compressed_text) + 7) // 8, byteorder='big')

    with open(output_path, 'wb') as output_file:
        pickle.dump((encoding_table, compressed_bytes), output_file)

def decompress_file(file_path, output_path):
    with open(file_path, 'rb') as file:
        encoding_table, compressed_bytes = pickle.load(file)

    compressed_text = bin(int.from_bytes(compressed_bytes, byteorder='big'))[2:]
    reverse_encoding_table = {code: char for char, code in encoding_table.items()}
    current_code = ""
    decompressed_text = ""

    for bit in compressed_text:
        current_code += bit
        if current_code in reverse_encoding_table.values():
            char = [k for k, v in reverse_encoding_table.items() if v == current_code][0]
            decompressed_text += char
            current_code = ""

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(decompressed_text)


def main():
    action = input("Что вы хотите сделать? (a - сжать файл, b - разжать): ")

    if action == 'a':
        file_name = input("Введите название файла для сжатия: ")
        compress_file(file_name, "compressed_file.huff")
    elif action == 'b':
        file_name = input("Введите название файла для разжатия: ")
        decompress_file("compressed_file.huff", file_name)
    else:
        print("Некорректный ввод. Пожалуйста, введите 'a' или 'b'.")

if __name__ == "__main__":
    main()
