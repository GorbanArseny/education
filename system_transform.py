fd16 = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'A': '10',
       'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}

td16 = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A',
        '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

def from16to10(s):
    count = 0
    res = 0
    s = s[::-1]
    for i in s:
        res = res + int(fd16[i]) * 16 ** count
        count += 1
    return res

def from10to16(s):
    res = []
    while s > 15:
        res = [s % 16] + res
        s = s // 16
    res = [s % 16] + res
    return ''.join([td16[str(i)] for i in res])

def from10to2(s):
    res = []
    while s > 1:
        res = [s % 2] + res
        s = s // 2
    res = [s % 2] + res
    return ''.join([str(i) for i in res])

def from10to8(s):
    res = []
    while s > 7:
        res = [s % 8] + res
        s = s // 8
    res = [s % 8] + res
    return ''.join([str(i) for i in res])