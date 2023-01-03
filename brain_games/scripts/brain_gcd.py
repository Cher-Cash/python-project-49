#!usr/bin/env python3
import prompt
import random
from ..cli import welcome_user
from .brain_games import greet


def gen():
    number = random.randint(1, 20)
    return number


def calculation(first, second):
    nod = 1
    if first > second:
        first, second = second, first
    for i in range(1, first + 1):
        if not first % i and not second % i:
            nod = i
    return nod


def main():
    greet()
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for i in range(0, 3):
        f_number = gen()
        s_number = gen()
        print(f'Question: {f_number} {s_number}')
        ans = prompt.string('Your answer: ')
        check = calculation(f_number, s_number)
        if check == int(ans):
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{check}'")
            print(f"Let's try again, {name}!")
            return 0
    print(f'Congratulations, {name}!')
