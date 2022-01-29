# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan_req = input('Введите номер VLAN: ')

file_name_r = 'CAM_table.txt'

result = []
k = 0

with open(file_name_r) as f_read:
    for line in f_read:
        if line.strip() and line.strip()[0].split()[-1][-1].isdigit():
            result.append(line.split())
            result[k][0] = int(result[k][0])
            k += 1
result.sort()
for i in result:
    vlan, mac, _, intf = i
    if vlan == int(vlan_req):
        print('{:<7}''{:<17}''{:<5}'.format(vlan, mac, intf))