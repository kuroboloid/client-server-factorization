# client-server-factorization
Клиент-серверное приложение по факторизации целых чисел.

Август 2018
Python 3.6
Клиент-серверное приложение по факторизации целых чисел. Проект 1.

Основные инструкции:

(1) Запустите приложение-сервер (server.py).
(2) Запустите приложение-клиент (client.py) с адресом и номером порта сервера.
(3) При появлении сообщения "Your number: " введите целое положительное число.
При неккорктном формате числа приглашение к вводу появится вновь. Для закрытия приложения введите "0".
(4) Отправьте число для факторизации на сервер, нажав клавищу <ENTER>.
На экране отобразится результат факторизации введеного числа.

Сообщения об ошибках:
1.  Сообщение: "Error connecting to server."
    Причина: Ошибка подключения к серверу.
    Способ устранения: Проверить, запущен ли сервер по адресу localhost:8080.
2.  Сообщение: "Uncorrect number!"
    Причина: Пользователем введено недопустимое значение.
    Способ устранение: Ввести целое положительное число.

Пример:
(1) $ python server.py
Server started at localhost:8080
(2) $ python client.py
Hello. Enter a positive integer for the factorization. To exit, enter "0".
(3) Your number: 1234567890
(4) <ENTER>
1234567890 = 2*1 + 3*2 + 5*1 + 3607*1 + 3803*1
(3) Your number: 689d
(4) <ENTER>
"Uncorrect number!"
(3) Your number: 689d
"Goodbye!"
