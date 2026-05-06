import sys
import os
import subprocess
import time
import random

difs = {'1': 'easy.txt', '2': 'medium.txt', '3': 'hard.txt'}
diff = {'1': 'легкая сложность', '2': 'умеренная сложность', '3': 'высокая сложность'}

def printscreen(res,gamedif,lifes,used):
    os.system('cls')
    print('ctrl + c - для закрытия программы')
    print(diff[gamedif])
    print(*res)
    print('проверенные буквы : ',*used)
    print(f'осталось попыток {lifes}')

def gamestart(gamedif):
    word = ''
    used = []
    with open(os.path.join('words',difs[gamedif]),'r',encoding='utf-8') as f:
        word = random.choice(f.read().strip().split())
    res = ['_' for i in range(len(word))]
    lifes = 5
    while lifes != 0 and '_' in res:
        printscreen(res,gamedif,lifes,used)
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

        pos = word.find(l)
        if pos == -1:
            lifes -= 1
        else:
            res[pos] = l
            pos = word[pos+1:].find(l)
            while pos != -1 and pos < len(word):
                res[pos] = l
                pos = word[pos+1:].find(l)
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
        if game == '1':
            gamestart(game)
        elif game == '4':
            sys.exit()
        else:
            os.system('cls')
            print('прочие режимы пока не доступны')
            input('нажмите любую клавишу для продолжения')
            os.system('cls')