#калькулятор
print("калькулятор")
a = int(input('первое число:'))
b = int(input('второе число:'))
d = int(input('выберете действие :\n 1 сложение\n 2 вычетание\n 3 умножение\n 4 деление\n'
    ' 5 возведение в степень \n'))
if d== 1:
    print('результат', a+b)
elif d==2:
   print('результат', a-b)
elif d==3:
    print('результат', a*b)
elif d==4:
    print('результат', a/b)
elif d==5:
    print('результат', a**b)

    # 2


n=int(input('введите число'))

simple = True

i = 2
while i < n:
    if n % i ==0:
        simple = False
    i += 1

if simple:
    print(' простое число')
else:
    print(' сложное число')

