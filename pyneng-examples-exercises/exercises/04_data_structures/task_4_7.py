# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
a=mac.split(':')

m1=bin(int(a[0], 16)) #сначала выполнил (a[0], 16) - указал, что AAAA это hex число. Затем преобразовал в bin
m2=bin(int(a[1], 16))
m3=bin(int(a[2], 16))

print(m1[2::] + m2[2::] + m3[2::])

