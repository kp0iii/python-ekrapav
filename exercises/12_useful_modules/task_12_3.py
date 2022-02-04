# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from tabulate import tabulate

reachable_ip = ["8.8.8.8", "8.8.4.4", "127.0.0.1"]
not_reachable_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9", "10.1.1.10"]


def print_ip_table(r_ip, nr_ip):
    table_result = {'Reachable': r_ip, 'Unreachable': nr_ip}
    print(tabulate(table_result, headers="keys"))


if __name__ == "__main__":
    print_ip_table(reachable_ip, not_reachable_ip)
