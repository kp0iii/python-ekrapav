# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


import subprocess

ip_list = [
    "8.8.8.8",
    "8.8.4.4",
    "127.0.0.1",
    "10.1.1.1",
]


def ping_ip_addresses(ip_address):
    ok = []
    nok = []
    for ip in ip_address:
        result = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.DEVNULL)
        if result.returncode:
            nok.append(ip)
        else:
            ok.append(ip)
    result_output = tuple([ok, nok])
    return result_output


if __name__ == "__main__":
    final_result = ping_ip_addresses(ip_list)
    print(final_result)
