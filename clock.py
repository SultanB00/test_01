time = int(input("Введите время в секундах: ")) #Задание 2
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f'чч:мм:сс   {hours} : {minutes} : {seconds}')