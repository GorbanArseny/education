import sys
import os
##оптимальный поиск через полиномиальное хеширование
x = 263
p = 1000000007

def hash(word):
    global x
    global p
    hash_value = 0
    word_lst = list(word)
    for i in range(len(word_lst)):
        hash_value = (hash_value + ord(word_lst[i]) * pow(x, i, p)) % p
    return hash_value

def hash_transform(prev_hash, left_char, right_char, pattern_len):
    global x, p
    hash_without_right = (prev_hash - ord(right_char) * pow(x, pattern_len - 1, p)) % p
    shifted_hash = (hash_without_right * x) % p
    new_hash = (shifted_hash + ord(left_char)) % p
    return new_hash

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('wrong arguments count')
        print('example: python log_analyzer.py sample.log error')
        sys.exit(0)

    file = sys.argv[1]
    word = sys.argv[2].lower()
    word_hash = hash(word)

    if not os.path.exists(file):
        print(f'no {file} file')
        sys.exit(0)
    print(f'try to find {word} in {file} by line')
    with open(file,'r') as f:
        line_number = 0
        for line in f:
            line_number += 1
            output_line = line.strip()
            line = line.strip().lower()
            line_hash = hash(line[len(line) - len(word):])
            result = []
            for i in range(len(line) - len(word), -1, -1):
                if word_hash == line_hash:
                    if word == line[i:i + len(word)]:
                        result.append(i)
                if i != 0:
                    line_hash = hash_transform(
                        line_hash,
                        line[i - 1],
                        line[i + len(word) - 1],
                        len(word)
                    )
            if len(result) != 0:
                print(f'{line_number}):',output_line)
                print(f'  {word} найдено в строке с началом в позициях:',*result)