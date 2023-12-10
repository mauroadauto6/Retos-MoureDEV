from numpy import *
import os
import time
import random

people = list()

while True:
    op = input("What do you want to do?\nAdd\nDelete\nShow\nSort\nExit\n-> ")
    if (op == 'Add'):
        name = input("Name:")
        if (name in people):
            print('This person already exists. Enter a new one')
            name = input("Name:") 
        people.append(name)
        os.system('cls')
    elif (op == 'Delete'):
        name = input("Name to delete:")
        if (name in people):
            people.remove(name)
            print(f'{name} was deleted')
            time.sleep(0.7)
        else: 
            print("This person doesn't exists")
            time.sleep(0.7)
        os.system('cls')
    elif (op == 'Show'):
        for p in people: 
            print(p)
        time.sleep(5)
        os.system('cls')
    elif (op == 'Sort'):
        num = random.randint(1, len(people))
        print(f'Selected {people[num]}')
        people.remove(people[num])
        time.sleep(1)
        os.system('cls')
    elif (op == 'Exit'):
        break