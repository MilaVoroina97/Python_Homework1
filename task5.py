# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.


# result = [[randint(1, 100) for j in range(m)] for i in range(n)]

from random import randint
def create_array(size,size2):
    array = []
    for i in range(size):
        buff = []
        for j in range(size2):
            value =  randint(1, 100)  #int(input('value'))
            buff.append(value)
        array.append(buff)
    return array


def printMatrix (matrix): 
   for i in range (len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:4d}".format(matrix[i][j]), end = "" ) 
      print ()

def sort_matrix(array):
    for i in range(len(array)- 1):
        for j in range(len(array)-i-1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
try:

    size = int(input('Введите количество строк массива: '))
    size2 = int(input('Введите количество столбцов массива: '))
    matrix = create_array(size,size2)
    printMatrix(matrix)
    x = len(matrix[0])#столбцы
    y = len(matrix)#строки

    table = []
    for i in range(y):
        for j in matrix[i]:
            table.append(j)

    sort_matrix(table)

    count = size2
    result = []
    start = 0
    end = count
    while end <= len(table):
        temp = []
        for i in range(start, end):
            temp.append(table[i])
        result.append(temp)
        start += count
        end += count
    print('Отсортированный массив:')
    printMatrix(result)
except:
    print('Введите, пожалуйста, целые числа.')





           




    


                
                

    




