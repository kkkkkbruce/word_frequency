#-------------------------------------------------------------------------------
# Name:        word_frequency.py
# Purpose:     strip a list of words excluding punctuation and numbers, then 
#              count the frequency of each word and write to a new file
#
# Author:      Kevin - vibe coded with the help of qwen2.5-coder:7b
#
# Created:     15/Sept/2026
# Copyright:   (c) Kevin 2026
# Licence:     MIT License
#-------------------------------------------------------------------------------
import string
from collections import Counter
import re
import sys
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def clean_text(text):
    translator = str.maketrans('', '', string.punctuation + '“”—¿¡‘’•')
    cleaned_text = text.translate(translator)
    cleaned_text = cleaned_text.lower()
    # Remove numerical digits
    cleaned_text = re.sub(r'\d+', '', cleaned_text)
    return cleaned_text
def count_word_frequency(text):
    words = text.split()
    return Counter(words)
def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
def main():
    if len(sys.argv) != 3:
        print("Usage: python word_frequency.py <input_file_path> <output_file_path>")
        sys.exit(1)
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    text = read_file(input_file_path)
    cleaned_text = clean_text(text)
    word_frequency = count_word_frequency(cleaned_text)
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    content = '\n'.join(f"{word}, {frequency}" for word, frequency in sorted_word_frequency)
    write_to_file(output_file_path, content)
if __name__ == "__main__":
    main()