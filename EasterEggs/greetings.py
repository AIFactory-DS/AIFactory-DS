import random
from time import localtime, time


def how_are_you():
    status = random.random()
    if status < 0.3:
        print("Good :)")
    elif status < 0.6:
        print("I'm alright")
    else:
        print("Let... let me go home...")


def hi():
    current_time = localtime(time())
    if current_time.tm_hour < 5:
        print("Why are you awake? Go to bed!")
    elif current_time.tm_hour < 12:
        print("Godmorgen!")
    elif current_time.tm_hour < 22:
        print("Godaften!")
    else:
        print("Godnat!")
