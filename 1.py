#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

n = int(input())
gerb = 0
orel = 0
for i in range(n):
    k = int(input())
    if k == 0:
        gerb += 1
    else:
        orel += 1

print(min(gerb, orel))