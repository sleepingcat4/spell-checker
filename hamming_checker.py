import csv

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def load_csv(filename):
    words = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append(row['Word'].lower())
    return words

def hamming_distance(word1, word2):
    if len(word1) != len(word2):
        return float('inf')
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
    return distance

def find_best_match(input_word, word_list):
    best_match = None
    min_distance = float('inf')
    for word in word_list:
        if len(word) == len(input_word):
            distance = hamming_distance(input_word, word)
            if distance < min_distance:
                min_distance = distance
                best_match = word
    return best_match

def build_prefix_tree(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie
