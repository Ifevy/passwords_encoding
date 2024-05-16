# лично у меня создаётся файл passwords.txt, но не открывается в vscode сразу. Надо через everything найти расположение файла 
# после первого рана и открыть файл ортдельно в вскоде. шифрованный файл key.key Тоже не открывается сам, его так же вручную надо открыть
# если с нуля запускать прогу, то надо убрать из скобок генерацию файла key, после первого рана положить обратно в скобки
# 



from cryptography.fernet import Fernet # шифруем, берет строку и преобразует её в рандомный текст который не имеет смысла. нам нужен ключ 


'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file: #создаём файл key.key написанный в байтах как переменную key_file и будет писать туда, создав через fernet Которая шифрует 
        key_file.write(key) # отбежать этот кусок кода единожды и добавить в строки'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key) 


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #'r' читает и наш знак '\n' за отдельную строчку. рстрипом мы убираем её
            user, passw = data.split('|')  # превращаем в список
            print('Юзер: ', user, '| Пароль: ', 
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Логин: ')
    pwd = input('Пароль: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n') 


while True:
    mode = input('Ты бы хотел добавить(add) новый пароль или глянуть(view) существующие? Для выхода нажми q. ').lower()
    if mode == 'q':
        break

    if mode == 'view': #пишу через If второй раз, т.к. по логике другой блок
        view()
    elif mode == 'add':
        add()
    else:
        print('Некорректный ввод :с')
        continue

