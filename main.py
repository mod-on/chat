import time
print("Взлом пароля от аккаунта")
n = int(input("Введите имя пользователя"))
for i in range(0,1001,1):
    print("Перебор паролей",str(i/10)+"%")
    time.sleep(0.001)
	
print("Ошибка, нехватает данных")
if input("2+2=") == "4":
    for i in range(0,100):
        print("Перебор паролей",str(i)+"%")
        time.sleep(0.1)
        print("Пароль: 1234")
        time.sleep(1000)
else:
    print("Неверные данные")
    time.sleep(1000)
