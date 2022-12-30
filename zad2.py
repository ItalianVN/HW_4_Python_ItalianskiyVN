# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prost_mnoj(n):
    my_list = list()
    delitel = 2
    while(delitel <= n):
        if(n % delitel) ==0:
            my_list.append(delitel)
            n = n/delitel
        else:
            delitel +=1
    return(my_list)
print(prost_mnoj(int(input('введите чсисло: '))))