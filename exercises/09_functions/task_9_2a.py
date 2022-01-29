# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}


def generate_trunk_config(trunk_config_template, trunk_mode_template):
    """
    - intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы
    такого вида:
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}
    - trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
    списка команд (список trunk_mode_template)

    Функция должна возвращать список команд с конфигурацией на основе указанных портов
    и шаблона trunk_mode_template. В конце строк в списке не должно быть символа
    перевода строки.
    """

    result = {}
    result_list = []
    for intf, vlan in trunk_config_template.items():
        for command in trunk_mode_template:
            if command.endswith('vlan'):
                result_list.append(command + ' ' + str(vlan).replace(' ', '').strip('[]'))
            else:
                result_list.append(command)
            result[intf] = result_list
        result_list = []
    return result


result_main = generate_trunk_config(trunk_config, trunk_mode_template)
print(result_main)
