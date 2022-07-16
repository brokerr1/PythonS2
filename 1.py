#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
# 6782 -> 23

number = int(input('Введите число:'))
result = 0
while (number > 0):
    result = result + (number % 10)
    number = number / 10
print("Сумма цифр в числе =", int(result))