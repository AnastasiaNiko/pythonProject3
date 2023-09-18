# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

N = int(input("Введите количество монет: "))

print("Массив монет: ")
from random import randint

array_coin = [randint(0, 1) for i in range(N)]
print(array_coin)


def score(N, array_coin):
    count1 = 0
    count0 = 0
    for i in range(N):
        if array_coin[i] == 1:
            count1 += 1
        else:
            if array_coin[i] == 0:
                count0 += 1
    return min(count1, count0)


print("Минимальное количество монет, которые нужно перевернуть ", score(N, array_coin))
