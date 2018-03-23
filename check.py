#! /usr/bin/env python
# -*- coding: utf-8 -*-
#сумма чисел
def sum(list):
	k=0
	sum = 0
	for i in list:
		list[k] = int(i)
		sum +=list[k]
		k+=1
	return sum
	
#четный числа
def even_number(list):
	k=0
	even_number = 0
	for i in list:
		list[k] = int(i)
		if list[k] % 2 == 0:
			even_number +=1
		k+=1
	return even_number

#не четный числа
def odd_number(list):
	odd_number = len(list)-even_number(list)
	return odd_number
	
#Малая группа/Большая группы
def SmallG(list, maxs):
	k=0
	d_min_max = {min:0, max:0}
	for i in list:
		list[k] = int(i)
		if list[k] < (maxs/2):
			d_min_max[min]+=1
		k+=1
	return (d_min_max[min])
	
#Большая группы/Малая группа
def GigG(list, maxs):
	k=0
	d_min_max = {min:0, max:0}
	for i in list:
		list[k] = int(i)
		if list[k] > (maxs/2):
			d_min_max[max]+=1
		k+=1
	return (d_min_max[max])