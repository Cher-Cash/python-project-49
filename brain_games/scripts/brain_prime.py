#!usr/bin/env python3
import prompt
import random
from ..cli import welcome_user
from .brain_games import greet


def gen():
    number = random.randint(1, 20)
    return number


def check(number):
    point = 0
    for i in range(1, number + 1):
        if not number % i:
            point += 1
    if point > 2:
        return 'no'
    return 'yes'


def main():
    greet()
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(0, 3):
        number = gen()
        task = check(number)
        print(f'Question: {number}')
        ans = prompt.string('Your answer: ')
        if task == ans:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{task}'")
            print(f"Let's try again, {name}")
            return 0
    print(f'Congratulations, {name}')
