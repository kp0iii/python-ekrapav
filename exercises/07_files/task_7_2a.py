# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

file_name = 'config_sw1.txt'

with open(file_name, 'r') as f:
    print('$ python task_7_2.py ' + file_name)
    for line in f:
        if not line.startswith('!'):
            for line_ign in ignore:
                if line_ign in line:
                    continue
                print(line.rstrip())
