# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


dict0 = {'access': 'Введите номер VLAN: ', 'trunk': 'Введите разрешенные VLANы: '}  


mode = input('Введите режим работы интерфейса (access/trunk): ')
ifn = input('Введите тип и номер интерфейса: ')
vl0 = dict0.get(mode) #почему не подставлялось через dict0[mode] я хз, почему то ругается, что это строка
vl = input(vl0)

acctmp = ((str('\n'.join(access_template))).format(vl))
trtmp = ((str('\n'.join(trunk_template))).format(vl))

#затем делаем словарик
dict1 = dict([('access', acctmp),('trunk', trtmp)])


print('interface {}'.format(ifn))
print(dict1[mode])

