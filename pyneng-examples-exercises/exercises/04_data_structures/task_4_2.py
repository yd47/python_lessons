# -*- coding: utf-8 -*-
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

mac1 = mac.replace(':','.')
print(mac1)

mac2 = mac.split(':')
print(mac2)

mac3 = '.'.join(mac2)
print(mac3)

mac4 = '!'.join(mac.split(':'))
print(mac4)
