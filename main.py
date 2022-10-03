import os.path
from os import path
from version import checkVersion


def check_api():
    if path.exists("TGapi.txt") == False:
        print('Введите свой api_id:')
        api_id = input()
        print('Введите свой api_hash:')
        api_hash = input()
        with open('TGapi.txt', 'w') as f:
            f.write(str(api_id)+'\n'+str(api_hash))
    else:
        print('АПИ установлен')

if __name__== "__main__":
    check_api()