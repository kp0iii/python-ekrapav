# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    """
    функцию get_int_vlan_map, которая обрабатывает конфигурационный
    файл коммутатора и возвращает кортеж из двух словарей:
    * словарь портов в режиме access, где ключи номера портов,
      а значения access VLAN (числа):
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/16': 17}

    * словарь портов в режиме trunk, где ключи номера портов,
      а значения список разрешенных VLAN (список чисел):
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
    """
    access = {}
    trunk = {}
    access_b = False
    with open(config_filename, 'r') as f:
        for line in f:
            if line.startswith('interface'):
                intf = line.rstrip().split()[-1]
                access_b = False
            elif line.strip().startswith('switchport mode access'):
                access_b = True
            elif access_b and line.strip().startswith('switchport access'):
                vlan = int(line.split()[-1])
                access[intf] = vlan
                access_b = False
            elif access_b:
                access[intf] = 1
            elif line.strip().startswith('switchport trunk allowed vlan'):
                vlan = line[31:].rstrip().split(',')
                vlan_result_trunk = [int(item) for item in vlan]
                trunk[intf] = list(vlan_result_trunk)
        print(access)
        print(trunk)


get_int_vlan_map('config_sw2.txt')
