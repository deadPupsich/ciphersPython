from affine import affine_encode, affine_decode
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
    print('При дешифровании вместо первого ключа шифрования, нужно вставить его мультипликационную пару.')
    key_a, key_b = input('Введите взаимопростые ключи по порядку через пробел: ').split()
    if method == 'Шифруем':
        print('Результат шифрования:', affine_encode(text, int(key_a), int(key_b), alphabet))
    elif method == 'Дешифруем':
        print('Результат расшифрования:', affine_decode(text, int(key_a), int(key_b), alphabet ))
    else:
        print('Error in method. You can only choose "Шифруем" or "Расшифровываем"')
        return

if __name__ == '__main__':
    main()