#!usr/bin/env python3
import prompt
import random
from ..cli import welcome_user
from .brain_games import greet


def gen():
    number = random.choice(range(1, 100, 1))
    return number


def main():
    greet()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        task = gen()
        print('Question:', task)
        answer = prompt.string('Your answer: ')
        if task % 2:
            check = 'no'
        else:
            check = 'yes'
        if check == answer:
            print('Correct!')
        else:
            print(f"'{answer}' wrong answer ;(. Correct answer was '{check}'")
            print("Let's try again,", name)
            return 0
    print(f'Congratulations, {name}!')
