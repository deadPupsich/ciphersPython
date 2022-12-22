from simpleSubstitutionCipher import simple_encode, simple_decode

def main():
    alphabet_std = 'abcdefghijklmnopqrstuvwxyz' # Стандартный алфавит.
    new_alphabet = alphabet_std[::-1] # Тот же алфавит, но перевёрнутый.
    method = input('Шифруем или Расшифровываем? ')
    text = input('Введите текст: ')
    if text == '':
        print('You need to enter text')
        return
    alphabet = input('Введите алфавит или выберете стандартный(:std) ')
    if alphabet == 'std':
        alphabet = alphabet_std
        alphabet_reverse = new_alphabet
    else:
        alphabet_reverse = alphabet[::-1]
    
    if method == 'Шифруем':
        print('Результат шифрования:', simple_encode(text, alphabet, alphabet_reverse))
    elif method == 'Дешифруем':
        print('Результат расшифрования:', simple_decode(text, alphabet, alphabet_reverse))
    else:
        print('Error in method. You can only choose "Шифруем" or "Расшифровываем"')
        return

if __name__ == '__main__':
    main()