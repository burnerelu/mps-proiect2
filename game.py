#!/usr/bin/env python

import os
import subprocess
import random
import time
import signal
import image
import PIL
from Tkinter import *
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
    lives = 5
    timeout = 15
    level = 1
    score = 0
    contor = 0
    image_to_display = image.ImageCreator()
    while lives > 0:
        os.system('clear')
        print "Level %d " % level
        if lives > 0:
            print "Lives %d " % lives
        print "Score %d\n\n\n " % score

        if level < 6:
            phrase = get_phrase(level)
            image_to_display.create(phrase, 0)
            #display = PIL.Image.open("current-img.png")
            os.system("wmctrl -T master$$ -r :ACTIVE: ; display current-img.png & sleep 0.1; wmctrl -r ImageMagick -e 0,0,0,-1,-1; wmctrl -a master$$")
            #display.show()
        else:
            difficulty = random.randint(1,4)
            if difficulty == 1:
                phrase = get_phrase(3)
                ### Rotate
            elif difficulty == 2:
                phrase = get_phrase(3)
                ### Minimize font
            elif difficulty == 3:
                phrase = get_phrase(random.randint(2,3))
            elif difficulty == 4:

                phrase = get_phrase(random.randint(1,2))
            image_to_display.create(phrase, difficulty)
            #display = PIL.Image.open("current-img.png")
            #display.show()
            os.system("wmctrl -T master$$ -r :ACTIVE: ; display current-img.png & sleep 0.1; wmctrl -r ImageMagick -e 0,0,0,-1,-1; wmctrl -a master$$")
        if raw_input_check(phrase, timeout):
            score += level + lives
        else:
            level -= 1
            lives -= 1
        level += 1
        contor = contor + 1
        if contor == 10:
            timeout = timeout - 1
            contor = 0

        os.system("pkill -9 display 2>/dev/null")
        os.remove("current-img.png")
    os.system('clear')
    print "Score: %d " % score
    high_score = score
    if not os.path.isfile("highscore.txt"):
        os.system("echo " + str(score) + " > highscore.txt")
    else:
        high_score = int(subprocess.Popen("cat highscore.txt", stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True).communicate()[0])
        if high_score < score:
            os.system("echo " + str(score) + " > highscore.txt")
            high_score = score

    print "Highscore: %d " % high_score
    

def main():

    play()

if __name__ == "__main__":
    main()
