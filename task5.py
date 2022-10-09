# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# from random import randint
# n = int(input('Введите количество строк массива: '))
# m = int(input('Введите количество столбцов массива: '))
# result = [[randint(1, 100) for j in range(m)] for i in range(n)]
# def printMatrix ( matrix ): 
#    for i in range ( len(matrix) ): 
#       for j in range ( len(matrix[i]) ): 
#           print ( "{:4d}".format(matrix[i][j]), end = "" ) 
#       print ()
# printMatrix(result)
# temp = 0
# for i in len(result):
#     for j in i:
#         for k in j-1:
#             if result[i][k] < result[i][k+1]:
#                 temp = result[i][k+1]
#                 result[i][k+1] = result[i][k]
#                 result[i][k] = temp
# printMatrix(result)

size = int(input('size'))
size2 = int(input('size'))
def create_array(size,size2):
    array = []
    for i in range(size):
        buff = []
        for j in range(size2):
            value = int(input('value'))
            buff.append(value)
        array.append(buff)
    return array

matrix = create_array(size,size2)

def printMatrix (matrix): 
   for i in range (len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:4d}".format(matrix[i][j]), end = "" ) 
      print ()
printMatrix(matrix)

def sort_matrix(array):
    min = array[0][0]
    temp = 0
    for i in range (len(array)):
        for j in range(len(array[i])):
            if min < array[i][j]:
                temp = min
                min = array[i][j]
                array[i][j] = temp
                return array

    

result = sort_matrix(matrix)
printMatrix(result)
                
                

    




