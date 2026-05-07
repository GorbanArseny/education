import sys
import os
import subprocess
import time
import random
import ast
import json

difs = {'1': 'easy.txt', '2': 'medium.txt', '3': 'hard.txt'}
diff = {'1': 'легкая сложность', '2': 'умеренная сложность', '3': 'высокая сложность'}

def printscreen(res,gamedif,lifes,used,category):
    os.system('cls')
    print('ctrl + c - для закрытия программы')
    print(diff[gamedif])
    print(f'тема загаданного слова :  {category}')
    print(*res)
    print('проверенные буквы : ',*used)
    print(f'осталось попыток {lifes}')

def get_word(gamedif):
    with open(os.path.join('words', difs[gamedif]), 'r', encoding='utf-8') as f:
        d = ast.literal_eval(f.read())
        category = random.choice(list(d.keys()))
        word = random.choice(d[category].strip().split(', '))
        return category,word

def gamestart(gamedif):
    word = ''
    used = []
    category,word = get_word(gamedif)
    res = ['_' for i in range(len(word))]
    lifes = 10
    while lifes != 0 and '_' in res:
        printscreen(res,gamedif,lifes,used,category)
        l = input('введите одну букву : ')

        if len(l) != 1:
            print('#########################################')
            print(f'необходимо ввести ОДНУ букву')
            input('нажмите любую клавишу для продолжения')
            continue
        if l in used:
            print('#########################################')
            print(f'буква {l} уже была проверена')
            input('нажмите любую клавишу для продолжения')
            continue
        else:
            used.append(l)

        if l in word:
            for i in range(len(word)):
                if word[i] == l:
                    res[i] = l  # открываем ВСЕ одинаковые буквы
        else:
            lifes -= 1
    print('#########################################')
    if lifes == 0:
        print('вы проиграли (((')
    else:
        print('вы победили !!!')
    print('#########################################')
    print(f'загаданное слово "{word}"')
    input('нажмите любую клавишу для продолжения')



if __name__ == '__main__':
    while True:
        os.system('cls')
        print('выберете сложность', '1 - легко', '2 - средне', '3 - сложно', '4 - выход', sep = '\n')
        game = input()
        if game in '123':
            gamestart(game)
        elif game == '4':
            os.system('cls')
            sys.exit()
        else:
            os.system('cls')
            print('прочие режимы пока не доступны')
            input('нажмите любую клавишу для продолжения')
            os.system('cls')
