import string
from _collections import defaultdict
import csv


def get_word_count(input_filename):
    '''
    Takes a text file as input and returns
    the word count as Python Dictionary
    '''
    with open(input_filename) as f_input:
        lines = f_input.readlines()
        word_dict = defaultdict(int)
        for line in lines:
            clean_line = remove_punctuation(line)
            for word in clean_line.split(' '):
                word_dict[word] += 1
    return word_dict


def remove_punctuation(my_str):
    '''
    Removes punctuation from string
    '''
    clean_str = my_str.translate(str.maketrans('', '', string.punctuation))
    return clean_str


def dict_to_file(my_dict, output_file, delimiter=','):
    with open(output_file, 'w') as f_output:
        writer = csv.writer(f_output, delimiter=delimiter)
        for key, value in my_dict.items():
            writer.writerow([key, value])

