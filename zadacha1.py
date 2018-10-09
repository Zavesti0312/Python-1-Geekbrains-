# coding : utf-8
__author__ = 'Алексей Юдин'

#задача 1

number = int(input("Введите любое число: "))
while number > 10:
        a = number//10
        print(number - 10*a)
        number = a
        
print (number)

a = number//10
b = number - (10*a)

