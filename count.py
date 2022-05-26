# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from msilib.schema import File
from typing import Counter


def read_file_content(filename):
    # [assignment] Add your code here

    with open(filename) as f:
        return Counter(f.read().split())


print("Number of words in the file :", read_file_content("test.txt"))


def count_words(read_file_content):
    text = read_file_content("./story.txt")

    # [assignment] Add your code here
d = dict()

for line in read_file_content:
    line = line.strip()

    line = line.lower()
    words = line.split(" ")

    for word in words:

        if word in d:

            d[word] = d[word] + 1
        else:

            d[word] = 1
for key in list(d.keys()):
    print(key, ":", d[key])
