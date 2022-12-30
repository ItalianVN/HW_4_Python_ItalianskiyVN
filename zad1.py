# Вычислить число c заданной точностью d. 
# Пример:
#     при d = 0.001,π = 3.141    10^(-1)≤d≤10^(-10).

from decimal import *
x = int(input('Введите количество знаков, после запятой число PI :> '))
getcontext().prec = x+1

def nilakantha(reps):
        result = Decimal(3.0)
        y = 1
        n = 2
        for n in range(2 ,2*reps+1 ,2):
                result += 4/Decimal(n*(n+1)*(n+2)*y)
                y *=-1
        return result

repetitions = 100
print(nilakantha(repetitions))