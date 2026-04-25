import sys
import os

if len(sys.argv) != 2:
    print('укажите путь к папке в параметрах при запуске')
    print('example: python sorter_back.py <path>}')
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print(f'dir {sys.argv[1]} not found')
    sys.exit()
os.chdir(sys.argv[1])
in_dir = os.listdir('.')
dirs = [i for i in in_dir if os.path.isdir(i)]
for d in dirs:
    if len(os.listdir(d)) != 0:
        for f in [i for i in os.listdir(d) if os.path.isfile(os.path.join(d,i))]:
            os.rename(os.path.join(d,f),os.path.join(os.getcwd(),f))
        if len(os.listdir(d)) == 0:
            os.rmdir(d)
        else:
            print(f'в папке {d} есть другие папки')