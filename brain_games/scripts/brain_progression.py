#!usr/bin/env python3
import prompt
import random
from ..cli import welcome_user
from .brain_games import greet


def gen():
    number = random.randint(1, 20)
    return number


def make(f_number):
    array = []
    prog = random.randint(1, 9)
    for i in range(0, 7):
        array.append(str(f_number))
        f_number += prog
    number = random.choice(array)
    ind = array.index(number)
    final_array = array[:ind]
    final_array.append('..')
    if ind == len(array) - 1:
        return number, final_array
    final_array.extend(array[ind + 1:])
    return number, final_array


def main():
    greet()
    name = welcome_user()
    print('What number is missing in the progression?')
    for i in range(0, 3):
        number = gen()
        task, array = make(number)
        array = ' '.join(array)
        print(f'Question: {array}')
        ans = prompt.string('Your answer: ')
        if task == ans:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{task}'")
            print(f"Let's try again, {name}")
            return 0
    print(f'Congratulations, {name}')
