from RSA import encrypt, decrypt, prime, keys
def main():
    method = input('Шифруем или Расшифровываем? ')
    if method == 'Шифруем':

        method_genpair = input('Шифрование с генерацией ключевой пары с помощью простых чисел или Шифрование с помощью ключевой пары; gen или pair: ')
        if method_genpair == 'gen':
            with open('текст.txt', 'r') as f:
                phrase = f.read()

            p, q = map(int, input('Введите два простых числа через пробел: ').split())

            if prime(p) == 0 or prime(q) == 0:
                raise TypeError('Одно из чисел не простое.')

            e, mod, d = keys(p, q)
            
            print(f'Открытый ключ: ({e}, {mod})\nЗакрытый ключ: {d}\nРезультат шифрования: {encrypt(e, mod, phrase)}')

        if method_genpair == 'pair':
            with open('текст.txt', 'r') as f:
                phrase = f.read()
            e, mod = map(int, input('Введите открытый ключ: ').split())
            d = int(input('Введите закрытый ключ: '))
            print(f'Результат шифрования: {encrypt(e, mod, phrase)}')

    if method == 'Расшифровываем':
        with open('шифртекст.txt', 'r') as f:
            text = f.read()
        d = int(input('Введите закрытый ключ: '))
        e, mod = map(int, input('Введите открытый ключ: ').split())
        print(f'Результат расшифрования: {decrypt(d, mod, text)}')


if __name__ == '__main__':
    main()

