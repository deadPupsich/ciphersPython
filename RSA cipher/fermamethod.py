import math
"""
!!!Важно
Метод Ферма для криптоанализа RSA применим в том случае, если
параметры р и q оказались близки друг к другу
"""
def keys(p: int, q: int, a: int):
    '''
    Def keys генерирует ключи.
    '''
    mod = p * q
    fi = (p - 1) * (q - 1)
    while True:
        if math.gcd(a, fi) == 1:
            break
        else:
            print('Попробуйте другое число.')
    d = 0
    for i in range(1, mod):
        if (a * i) % fi == 1:
            d = i
            break
    return d

a, b = input('Введите открытый ключ: ').split()
a, b = int(a), int(b)
b1 = b
b = round(math.sqrt(b)) + 1
c = 0
cnt = 1
while True:
    c = math.sqrt(abs(b ** 2 - b1))
    if int(c) == c:
        print('t =', b)
        print('V =', c)
        print(f'кол-во итераций - {cnt}')
        break
    b += 1
    cnt += 1

p = b + c
q = b - c 
print(f' p = {p}\n q = {q}\n N = {int(p * q)}\n Закрытый Ключ - {keys(int(p), int(q), a)}')
