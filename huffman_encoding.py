def calculate_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    # Arrange the frequencies in descending order
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequencies

def build_priority_queue(frequencies):
    # frequencies is a list of tuples, so convert it to the correct format for the heap
    heap = [[weight, [char, ""]] for char, weight in frequencies]
    heap.sort(key=lambda x: x[0])
    return heap

def build_huffman_tree(heap):
    while len(heap) > 1:
        lo = heap.pop(0)
        hi = heap.pop(0)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        new_node = [lo[0] + hi[0]] + lo[1:] + hi[1:]
        heap.append(new_node)
        heap.sort(key=lambda x: x[0])
    return heap[0]

def generate_huffman_codes(tree):
    huffman_codes = {}
    for char, code in tree[1:]:
        huffman_codes[char] = code
    return huffman_codes

def huffman_encode(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

def huffman_decode(encoded_text, huffman_codes):
    reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ""
    decoded_text = ""
    
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_huffman_codes:
            decoded_text += reverse_huffman_codes[current_code]
            current_code = ""
    
    return decoded_text

# Read the text file
with open('text_project_Huffman.txt', 'r') as file:
    text = file.read()

frequencies = calculate_frequencies(text)
print("Frequencies:\n", frequencies)

heap = build_priority_queue(frequencies)
print("Heap:\n", heap)

huffman_tree = build_huffman_tree(heap)
print("Huffman Tree:\n", huffman_tree)

huffman_codes = generate_huffman_codes(huffman_tree)
print("Huffman Codes:\n", huffman_codes)

encoded_text = huffman_encode(text, huffman_codes)
print("Encoded Text:\n", encoded_text)

decoded_text = huffman_decode(encoded_text, huffman_codes)
print("Decoded Text:\n", decoded_text)
