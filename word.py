#!/usr/bin/env python
import random
import os

def main():
    phrase = ""
    files = os.listdir("words")
    letter_file = "words/" + random.choice(files)
    letter = open(letter_file, "r")
    words = letter.readlines()
    phrase = phrase + random.choice(words).rstrip("\n")
    letter.close()


    print phrase


if __name__ == "__main__":
    main()
