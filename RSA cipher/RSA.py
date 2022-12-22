from math import gcd


def prime(j: int) -> int:
    '''
    Def prime проверяет число j на простоту.
    '''
    k = 0
    for i in range(1, j+1):
        if j % i == 0:
            k += 1
    if k <= 2:
        return j


def keys(p: int, q: int):
    '''
    Def keys генерирует ключи.
    '''
    mod = p * q
    fi = (p - 1) * (q - 1)
    while True:
        e = int(input(f'Введите целое число, взаимно простое с {fi}: '))
        if gcd(e, fi) == 1:
            break
        else:
            print('Попробуйте другое число.')
    d = 0
    for i in range(1, mod):
        if (e * i) % fi == 1:
            d = i
            break
    return e, mod, d


def encrypt(e: int, mod: int, text: str) -> list:
    encrypted_list = []

    for i in range(len(text)):
        encrypted_list.append(((ord(text[i]) ** e) % mod))

    return encrypted_list



def decrypt(d: int, mod: int, text: str) -> str:
    decrypted_list = []
    new_text = text[1 : -1]
    arr = new_text.split(', ')

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    for i in range(len(arr)):
        decrypted_list.append((arr[i] ** d) % mod)
    decrypted_text = ''

    for j in range(len(decrypted_list)):
        decrypted_text += chr(decrypted_list[j])
    return decrypted_text
