# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from pprint import pprint

with open('ospf.txt', 'r') as f:
    for line in f:
        _, ip, metric, _, next_h, last_upd, intf = line.split()
        print('{:<20}{}\n' \
             '{:<20}{}\n' \
             '{:<20}{}\n' \
             '{:<20}{}\n' \
             '{:<20}{}\n'.format("Prefix", ip,
                               "AD/Metric", metric.strip('[]'),
                               "Next-Hop", next_h.strip(','),
                               "Last update", last_upd.strip(','),
                               "Outbound Interface", intf))
