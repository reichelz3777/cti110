# Math Quiz
# 4/23/2022
# CTI-110 P5HW2 - Math Quiz
# Zachary Reichel
#

import random

def addition():
    num1 = random.randint(11,50)
    num2 = random.randint(11,50)
    print(f' {num1}')
    print(f'+{num2}')
    print('Enter answer.')
    ans = int(input())
    if ans != (num1 + num2):
        print('Sorry, your guess is not correct.')
        print("The correct answer is",+(num1+num2))
        print('\n')
    else:
        print('Congratulations!!!! your answer is correct...\n')

def subtraction():
    num1 = random.randint(11, 50)
    num2 = random.randint(11, 50)
    if num1<num2:num1,num2=num2,num1
    print(f' {num1}')
    print(f'-{num2}')
    print('Enter answer.')
    ans = int(input())
    if ans != (num1 - num2):
        print('Sorry, your guess is not correct.')
        print("The correct answer is",+(num1-num2))
        print('\n')
    else:
        print('Congratulations!!!! your answer is correct...\n')

def main():
    print('Welcome to Math Quiz\n')
    while True:
        print('MAIN MENU')
        print('-------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit\n')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            addition()
        elif choice == '2':
            subtraction()
        elif choice == '3':
            print('Thank you for playing...\nBye!!')
            break

main()
