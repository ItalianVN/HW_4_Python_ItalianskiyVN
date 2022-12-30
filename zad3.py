from random import randint



numbers = [randint(1, 10) for i in range (int(input('введите число: ')))]
print(numbers)
print([x for x in numbers if numbers.count(x)==1])

