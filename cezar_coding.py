def cez_ru(sym,pos):
    if sym.isupper():
        sup = 1040
    else:
        sup = 1072
    code = ord(sym)
    code = code - sup
    new_code = (code + pos + 32)%32
    return chr(new_code+sup)

def cez_en(sym,pos):
    if sym.isupper():
        sup = 65
    else:
        sup = 97
    code = ord(sym)
    code = code - sup
    new_code = (code + pos + 26)%26
    return chr(new_code+sup)

def st_transform(st,pos,ru):
    if ru:
        cez = lambda s,p: cez_ru(s,p)
    else:
        cez = lambda s,p: cez_en(s,p)
    lst = list(st)
    for i in range(len(lst)):
        if lst[i].isalpha():
            lst[i] = cez(lst[i],pos)
    return ''.join(lst)

st = 'Y'
for i in range(4,5):
    print(st_transform(st,i,False))