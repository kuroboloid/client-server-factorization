#!/usr/bin/python
import socket
from sympy.ntheory import factorint


def multipliers(n):
    """Разложение на множители.

    Параметры:
    n : int
        Целое число для факторизации.

    Выходные данные:
    str: string
        Строка разложения на множители.
    """
    mult = factorint(n)                                 # Получение словаря простых множителей числа n.
    l = []
    for key in mult:
        l.append(str(key) + "*" + str(mult[key]))
    return (str(n) + " = " + " + ".join(l))

def send_answer(conn, data=""):
    """Отправить ответ клиенту.

    Параметры
    conn :
        Сокет клиента.
    data :  string
        Сообщение клиенту.
    """
    data = data.encode("utf-8")
    conn.send(data)

def parse(conn):
    """Обработка пользовательского запроса.

    Параметры
    conn :
        Сокет клиента.
    """
    try:
        data = conn.recv(1024)
        if not data:
            return  #
    except:
        return
    udata = int(data.decode("utf-8"))
    answer = multipliers(udata)
    send_answer(conn, data=answer)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Создать сервер.
    server_address = ('', 8080)                                     # Сервер работает по адресу localhost:8080.
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)                                       # Инициализация ip-адреса и порта.
    sock.listen(1)                                                  # Кол-во клиентских соединений (1).
    print("Server started at localhost:8080.")
    try:
        while 1:
            try:
                client, addr = sock.accept()                        # Соединение с клиентом.
            except socket.error:
                send_answer(client, data="Error connecting to server.")
                pass
            else:
                parse(client)                                       # Обработка пользовательского запроса.
            finally:
                client.close()
    finally:
        sock.close()

