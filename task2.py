# задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True,False]:
    for y in[True,False]:
        for z in[True,False]:
            print(f'Проверка истинности утверждения значения предикат:{x,y,z} : {not(x or y or z) == (not x and not y and not z)}')
            

        

