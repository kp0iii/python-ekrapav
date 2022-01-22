# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

port_mode = input('Введите режим работы интерфейса (access/trunk): ')
if_ip = input('Введите тип и номер интерфейса: ')

d_keys = ['access_template', 'trunk_template']
template = dict.fromkeys(d_keys)
template = dict(access=access_template, trunk=trunk_template)
question_vlan = {'access': 'Введите номер VLAN: ', 'trunk': 'Введите разрешенные VLANы: '}
vlan = input(str(question_vlan[port_mode]))
print('interface {}\n'.format(if_ip) + str(template[port_mode])
      .replace("'", "").replace("]", "").replace("[", "").replace(', ', '\n').format(vlan))