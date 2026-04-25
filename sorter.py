import sys
import os

if len(sys.argv) != 2:
    print('укажите путь к папке в параметрах при запуске')
    print('example: python sorter.py <path>}')
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print(f'dir {sys.argv[1]} not found')
    sys.exit()
os.chdir(sys.argv[1])
in_dir = os.listdir('.')
files = [i for i in in_dir if os.path.isfile(i)]
for i in files:
    pars = i.split('.')
    if not os.path.exists(pars[1]):
        os.mkdir(pars[1])
    os.rename(i,os.path.join(pars[1],i))