password = 1936 #задаем значение пароля
a = input("Введите пароль:") #запрашиваем у пользователя пароль
if password == a: #используем if и задаем для него условие
    print("Доступ разрешен") #выводится при правильном пароле
else:  #используем else если первое условие не верно и задаем значение
    print("Доступ запрещен")  #выводится если пароль введен не верно
