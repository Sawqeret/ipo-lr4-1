number = int("Введите целое число: ") # запрашиваем у пользователя целое число
print("Четные числа от 0 до", number, ":") # выводим пользователю, четные числа от 0 и до его введенного числа
for i in range(0, number +1): # используем цикл for для перебора чисел от 0 до введеного числа пользователем включительно
      if i % 2 == 0: #проверяем четное ли число 
    print(i) # выводятся если число четное
