from affineReccurentCipher import affine_reccurent_encode, affine_reccurent_decode

def main():
    alphabet_std = 'abcdefghijklmnopqrstuvwxyz'
    method = input('Шифруем или Расшифровываем? ')
    text = input('Введите текст: ')
    if text == '':
        print('You need to enter text')
        return
    alphabet = input('Введите алфавит или выберете стандартный(:std) ')
    if alphabet == 'std':
        alphabet = alphabet_std
    key_a1, key_a2, key_b1, key_b2 = input('Введите ключи по порядку через пробел: ').split()
    if method == 'Шифруем':
        print('Результат шифрования:', affine_reccurent_encode(text, alphabet, int(key_a1), int(key_a2), int(key_b1), int(key_b2)))
    elif method == 'Дешифруем':
        print('Результат расшифрования:', affine_reccurent_decode(text, alphabet, int(key_a1), int(key_a2), int(key_b1), int(key_b2)))
    else:
        print('Error in method. You can only choose "Шифруем" or "Расшифровываем"')
        return


if __name__ == '__main__':
    main()
