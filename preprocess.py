import csv

def csv_to_list(csv_file):
    words = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            words.append(row['Word'])
    return words

def save_text(word_list, output_file):
    with open(output_file, 'w') as file:
        for word in word_list:
            file.write(word + '\n')

csv_file = 'OPTED-Dictionary.csv'
output_file = 'word_processed.txt'

words_list = csv_to_list(csv_file)
save_text(words_list, output_file)
