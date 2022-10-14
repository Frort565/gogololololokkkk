from random import randint

n = randint(4, 30)
z = n
print(' изначальное колличество камней в куче', n)
while True:
    if n <= 4:
        break
    n -= randint(1, 3)
    print('камней в куче', n)
    if n <= 3:
        break
    print('введите число от 1 до 3')
    n -= int(input())
if n == 4:
    print('введите число от 1 до 3')
    n -= int(input())
    print('Вы проиграли')
elif n < 3:
    print('введите число от 1 до 3')
    b = int(input())
    if b >= n:
        print('Вы выиграли')
    else:
        print('Вы проиграли')