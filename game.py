#!/usr/bin/env python

import os
import subprocess
import random
import time
import signal


def alarmHandler():
    pass

def raw_input_check(phrase, timeout=10):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = raw_input()
        signal.alarm(0)
        if text == phrase:
            return True
        else:
            return False
    except:
        print '\nPrompt timeout. Continuing...'
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

def get_word():
    process = subprocess.Popen("python word.pyc", shell=True, 
              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.communicate()[0].rstrip('\n')


def get_phrase(number_of_words):
    phrase = ""
    for i in range(0, number_of_words):
        phrase += get_word() + " "
    return phrase.rstrip(' ')


def return_false(timer):
    timer.cancel()
    return False

def play():
    lives = 3
    level = 1
    score = 0
    while lives > 0:
        if level < 7:
            phrase = get_phrase(level)
            print phrase
        else:
            difficulty = random.randint(1,3)
            if difficulty == 1:
                phrase = get_phrase(3)
                ### Rotate
            elif difficulty == 2:
                phrase = get_phrase(3)
                ### Minimize font
            else:
                phrase = get_phrase(7)
            print phrase
        if level % 10 == 0:
            lives += 1
        if raw_input_check(phrase, 10):
            score += level + lives
        else:
            level -= 1
            lives -= 1
        level += 1
        os.system('clear')
        print "Level %d " % level
        if lives > 0:
            print "Lives %d " % lives
        print "Score %d\n\n\n " % score


def main():

    play()

if __name__ == "__main__":
    main()
