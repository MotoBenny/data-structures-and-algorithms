# from data_structures.hashtable import Hashtable
import re


def first_repeated_word(word):
    # separate the words at the spaces
    pattern = re.compile('[^a-zA-Z ]')
    stripped = pattern.sub('', word)
    words = stripped.lower().split()
    # print(stripped)
    check_set = set()

    for word in words:
        if word in check_set:
            return word
        else:
            check_set.add(word)







# This was my first go, worked for everything but the punctuation. . .
# def first_repeated_word(word):
#     # separate the words at the spaces
#
#     words = word.lower().split()
#     check_set = set()
#     print( words)
#     for word in words:
#         if word in check_set:
#             return word
#         else:
#             check_set.add(word)
