# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
var = ospf_route.split()

template = ['Protocol: {Prot:>15}',
	'Prefix: {Prefix:>25}',
	'AD/Metric: {Metric:>16}',
	'Next-Hop: {NextHop:>21}',
	'Last update: {Update:>14}',
	'Outbound Interface: {OIF:>16}']


'''
print(template.format(Prot=var[0].replace('O', 'OSPF'), Prefix=var[1], 
Metric=(var[2].strip('[]')), NextHop=var[4], Update=var[5], OIF=var[6]))
'''

print('\n'.join(template).format(Prot=var[0].replace('O', 'OSPF'), Prefix=var[1], 
Metric=(var[2].strip('[]')), NextHop=var[4], Update=var[5], OIF=var[6]))
