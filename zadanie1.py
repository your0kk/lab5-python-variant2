numbers = []

while True:
    number = int(input("Введите целое число (0 - конец ввода): "))
    if number == 0:
        break
    numbers.append(number)

numbers.sort(reverse=True)

print("Числа по убыванию:")
for number in numbers:
    print(number)
