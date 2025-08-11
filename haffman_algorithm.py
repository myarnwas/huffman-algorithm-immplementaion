import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    # للمقارنة بين العقد في الـ heap
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    freq = defaultdict(int)
    for ch in text:
        freq[ch] += 1
    return freq

def build_huffman_tree(freq_table):
    heap = [HuffmanNode(freq, char) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    return heap[0]

def build_codes(root):
    codes = {}

    def generate_codes(node, current_code=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root)
    return codes

def huffman_encode(text, codes):
    return "".join(codes[ch] for ch in text)

def huffman_decode(encoded_text, root):
    decoded = []
    node = root
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded.append(node.char)
            node = root
    return "".join(decoded)


# تجربة
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    freq_table = build_frequency_table(text)
    root = build_huffman_tree(freq_table)
    codes = build_codes(root)
    encoded = huffman_encode(text, codes)
    decoded = huffman_decode(encoded, root)

    print("Original text:", text)
    print("Encoded text:", encoded)
    print("Decoded text:", decoded)
