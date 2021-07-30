# Заполняем данные
account1 = {'login' : 'ivan', 'password' : 'q1'}
account2 = {'login' : 'petr', 'password' : 'q2'}
account3 = {'login' : 'olga', 'password' : 'q3'}
account4 = {'login' : 'anna', 'password' : 'q4'}

user1 = {'name' : 'Иван', 'age' : 20, 'account' : account1}
user2 = {'name' : 'Петр', 'age' : 25, 'account' : account2}
user3 = {'name' : 'Ольга', 'age' : 18, 'account' : account3}
user4 = {'name' : 'Анна', 'age' : 27, 'account' : account4}

user_list = [user1, user2, user3, user4]
aver_age = 0


# 1
#Запрашиваем у пользователя ключ
query1 = input('Введите ключ (name или account): ')

#Выводим информацию по ключу или сообщение, что ключ не верный
try:
    key = query1.lower()
    count = 0
    for i in user_list:
        count += 1
        print(f'значение ключа {key} для юзера {count} = {i[key]}')

except KeyError:
    print('Введенный ключ не найден\n')
except:
    print('Другая ошибка\n')

print('')

#2
# Запрашиваем порядковый номер
query2 = input('Введите порядковый номер: ')

#Выводим информацию о пользователе или сообщение об ошибке
try:
    # получаем данные или ловим ошибку
    user_number = int(query2) - 1
    user_name = user_list[user_number]['name']
    user_age = user_list[user_number]['age']
    user_login = user_list[user_number]['account']['login']
    user_pass = user_list[user_number]['account']['password']

    #выводим полученне данные
    print('Данные по юзеру №' + query2)
    query2 = int(query2) - 1
    print('имя: ' + user_name)
    print('возраст: ' + str(user_age))
    print('логин: ' + user_login)
    print('пароль: ' + user_pass + '\n')
except IndexError:
    print('Пользователь с указанным номером не найден\n')
except ValueError:
    print('Некорректно введён номер пользователя\n')
except:
    print('Другая ошибка\n')


#3
#Кого переносим в конец?
end_user_number = int(input('Введите номер пользователя, которого нужно перенести в конец: '))-1
print('Список до изменения: ')
print(user_list)

#Убираем пользователя из списка, но запоминаем
end_user = user_list.pop(end_user_number)

# добавляем пользователя в конец
user_list.append(end_user)

print(f'Пользователь был перемещён в конец: \n{user_list} \n')




#4 cредний возраст
count = 0
for i in user_list:
    count += 1
    aver_age += i['age']

print(f'Средний возраст пользователей: {aver_age/count}')
