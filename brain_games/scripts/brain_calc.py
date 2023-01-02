#!usr/bin/env python3
import prompt
import random
from ..cli import welcome_user
from .brain_games import greet


def gen():
    number = random.randint(1, 20)
    return number


def calculation(operator, first, second):
    if operator == '+':
        return first + second
    if operator == '-':
        return first - second
    if operator == '*':
        return first * second


def main():
    greet()
    operations = '+-*'
    name = welcome_user()
    print('What is the result of the expression?')
    for i in operations:
        f_number = gen()
        s_number = gen()
        task = random.choice(operations)
        print(f'Question: {f_number} {task} {s_number}')
        ans = prompt.string('Your answer: ')
        check = calculation(task, f_number, s_number)
        if check == int(ans):
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{check}'")
            print("Let's try again,", name)
            break
