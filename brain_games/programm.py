#!usr/bin/env python3
import prompt
import random
import cli


def gen():
    number = random.choice(range(1, 100, 1))
    return number


def game():
    count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 0:
        task = gen()
        print('Question: ', task)
        answer = prompt.string('Your answer: ')
        if task % 2:
            check = 'no'
        else:
            check = 'yes'
        if check == answer:
            count -= 1
            print('Correct!')
        else:
            print("'", answer, "' ", 'wrong answer ;(. Correct answer was ', "'", check, "'")
            print("Let's try again, ", cli.name)
            break
    print('Congratulations, ', cli.name, '!')
