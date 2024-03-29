# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите IP-адрес в формате 10.0.1.1: ')

if ip.replace('.', '').isnumeric() == False or ip.count('.') != 3:
    print('Неправильный IP-адрес')
elif 0 < int(ip.split('.')[0]) > 255 or 0 < int(ip.split('.')[1]) > 255 \
        or 0 < int(ip.split('.')[2]) > 255 or 0 < int(ip.split('.')[3]) > 255:
    print('Неправильный IP-адрес')
else:
    if 1 <= int(ip.split('.')[0]) <= 223:
        print('unicast')
    elif 224 <= int(ip.split('.')[0]) <= 239:
        print('multicast')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    else:
         print('unused')
