# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'


vlans1 = command1.split()
vlans2 = command2.split()

'''
str1 = vlans1[4]
str2 = vlans2[4]

split1 = str1.split(',')
split2 = str2.split(',')

set1 = set(split1)
set2 = set(split2)

result = sorted(set1&set2)
'''

#оно же:
set1 = set(vlans1[4].split(','))
set2 = set(vlans2[4].split(','))
result = sorted(set1&set2)

print(result)

