import socket

def correct(usernum):
    """Проверка ввода пользователя на корректность.

    Параметры
    usernum : string
        Введенное число."""
    data = usernum.encode('utf-8')
    if data.isdigit():                                          #Проверка, состоит ли только из цифр.
        return data
    else:
        return ""


if __name__ == '__main__':
    print('Hello. Enter a positive integer for the factorization. To exit, enter "0".')
    while 1:
        conn = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
        server_address = ('localhost', 8080)                    # Параметры сервера.
        try:
                conn.connect(server_address)                    # Соединиться с сервером.
        except:
                print('Error connecting to server.')
                conn.close()
                exit()
        try:
            while 1:
                data = correct(input("Your number: "))          #Ввод числа пользователем.
                if data:
                    break
                else:
                    print("Uncorrect number!")
            if data == b"0":
                print("Goodbye!")
                conn.close()
                exit()
            conn.send(data)                                     # Отправить число на сервер.
            conn.settimeout(5)                                  # Установка таймаута ответа сервера (5 секунд).
            rec = conn.recv(1024)                               # Получить ответ от сервера.
            if not rec:
                conn.close()
        except socket.error:
            break
        else:
            print(rec.decode("utf-8"))
        finally:
            conn.close()

