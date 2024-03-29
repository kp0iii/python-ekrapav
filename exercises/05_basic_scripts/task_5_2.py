# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите IP-сеть в формате: 10.1.1.0/24: ')
mask = ip[int(ip.find('/'))+1:]
mask_bin = '1' * int(mask) + '0'* (32 - int(mask))
ip = ip[:int(ip.find('/'))]
ip_dec = ip.split('.')
print('Network:\n{:<8}  {:<8}  {:<8}  {:<8}\n'
      '{:08b}  {:08b}  {:008b}  {:08b}'
      .format(int(ip_dec[0]), int(ip_dec[1]), int(ip_dec[2]), int(ip_dec[3]),
              int(ip_dec[0]), int(ip_dec[1]), int(ip_dec[2]), int(ip_dec[3])))
print('Mask:\n/'+mask+'\n'
      '{:<8}  {:<8}  {:<8}  {:<8}\n'
      '{:8}  {:8}  {:8}  {:8}'
      .format(int(mask_bin[:8], 2), int(mask_bin[8:16], 2), int(mask_bin[16:24], 2), int(mask_bin[24:], 2),
              mask_bin[:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:]))
