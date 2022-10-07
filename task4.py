# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию,
# после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

def calculator():
    x = float(input('Введите, пожалуйста, первое число:'))
    y = float(input('Введите второе число: '))
    operation = input('Введите операцию для выполнения вычислений с числами: ')
    if (y == 0 and operation == '/') or (y == 0 and operation == 'div') or (y == 0 and operation =='//') or(y == 0 and operation == 'mod'):
        print('Делить на 0 нельзя.')
    elif operation == '+':
        print(x + y)
    elif operation == '-':
        print(x - y)
    elif operation == '/':
        print(x / y)
    elif operation == '*':
        print(x * y)
    elif operation == 'mod' or operation == '%':
        print(x % y)
    elif operation == 'pow' or operation == '**':
        print(x ** y)
    elif operation == 'div' or operation == "//":
        print(x // y)
    else:
        print('Введите пожалуйста допустимые операции для вычисления:  +, -, /, *, mod, pow, div')

try:
    calculator()
except:
    print('Введите, пожалуйста, именно числа и знаки операций.')
