import math

a, b = int(input()), int(input())
b1 = b
b = round(math.sqrt(b)) + 1
print(b)
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
print(f'p = {p} q = {q} N = {int(p * q)}')
