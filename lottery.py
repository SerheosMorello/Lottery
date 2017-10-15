from random import randint
from check import *
import os
#MySet = input('Enter 5 numbers from 1 to 49: ')
#MySet = MySet.split(" ")
# Инициализация переменных
gameagen = True
count = 1
countnum = 6 # количество номеров игрока
maxnum = 50 # максимальное число номеров в игре
diver = 10000 # отображение игр кратных значению 
allBols = [x for x in range(1,maxnum)]
GameSet = []
MySet = []
counterwiner = {x : 0 for x in range(0, countnum+1)}
statistic = {x : 0 for x in range(1,maxnum)}
level = 4 # количество совпадений для записи в файл result
initval = 0 # инициализация значений для лотереи (0/1)
def init(values):
	'''	Устанавливаем параметры для игры'''
	if values == 1:
		global countnum, counterwiner, diver, maxnum, level, allBols, statistic
		
		countnum = int(input('Количество чисел в наборе: '))
		maxnum = int(input('Количество чисел в игре: '))
		
		counterwiner = {x : 0 for x in range(0, countnum+1)}
		allBols = [x for x in range(1,maxnum+1)]
		statistic = {x : 0 for x in range(1,maxnum+1)}
		diver = int(input('Введите число, кратный номер игры будет отображен на экране: '))
		level = int(input('Введите число, совпавшее количесво шаров будет сохранено в файл: '))
	else: pass

# Показать статистику
def showstatistic():
	'''Метод выводит статистику выпадения'''
	for i in statistic.keys():
		print(str(i) + ' выпал ' +str(statistic[i]) + ' раза : ' +  str(statistic[i]/(count*countnum)) + '%')	
# Сохраняет результаты в файл
def saveresult(filapath):
	'''Сохраняет результат игры  в файл, путь к файлу'''
	f = open(filapath+".csv", 'a', encoding="utf-8")
	if os.path.getsize(filapath+'.csv') == 0:
		f.write('Номер игры,')
		k=1
		for i in MySet:
			f.write('Номер '+ str(k) + ',')
			k+=1
		k=1
		f.write('Количество совпадений,')
		for i in GameSet:
			f.write('Номер '+ str(k) + ',')
			k+=1
		f.write('\n')
		
	f.write(str(count)+',')
	for i in list(MySet):
		f.write(str(i)+',')
	f.write(str(countnum -len(set(MySet) - set(GameSet)))+',')
	for i in list(GameSet):
		f.write(str(i)+',')
	f.write('\n')
	f.close()
# Выводит результаты на экран
def showresult(status): 
	'''Метод показывает результат игры, status - результат игры (0/1) (Игра окончена/Игра продолжается)'''
	if status == 0:
		print('Розыгрыш № '+ "{:,}".format(count) + ' Игра окончена')
	else: 
		print('Розыгрыш № '+ "{:,}".format(count) + ' игра продолжается...')
	print(' Выпавшая комбинация: ' +str(GameSet))
	print(' Ваша комбинация:    '+str(MySet))
	print("Сумма="+ str(sum(MySet)) + " Ч/НЧ=" + str(even_number(MySet)) + "/" + str(odd_number(MySet)) + " MГ=" + str(SmallG(MySet, maxnum-1)) + " БГ=" + str(GigG(MySet, maxnum-1)) + " Совпало=" +str(countnum-len(set(MySet) - set(GameSet))) )
	for i in counterwiner:
		print(str(countnum - i) +' совпадений '+ "{:,}".format(counterwiner.get(i)) + ' : ' + str(counterwiner.get(i)/count) + '%')

# уровень легирования
def loglevel(level):
	'''loglevel(level) - подробность записи выпавших комбинация, где level - число совпавших чисел у MySet с GameSet'''
	if int(len(set(MySet) - set(GameSet))) <= countnum-level:
		saveresult('Result')
#_____________________________________
init(initval)

print('Игра началась, результаты будут показаны после ' +"{:,}".format(diver) + ' сыгранных партий')
while gameagen:
	# Генерация комбинации партии
	GameSet = [allBols[randint(0,len(allBols)-1)] for x in range(countnum)]
	while len(GameSet) != len(set(GameSet)):
		GameSet = [allBols[randint(0,len(allBols)-1)] for x in range(countnum)]
	for i in GameSet:
		statistic[i]+=1
	#GameSet = [1, 11, 23, 33, 41, 24]
	#GameSet.sort()
	
	# Генерация партии игрока
	MySet = [allBols[randint(0,len(allBols)-1)] for x in range(countnum)]
	while (len(MySet) != len(set(MySet))): #or (not 126<sum(MySet)<167)	or (even_number(MySet) != odd_number(MySet)) or not (2==SmallG(MySet, maxnum-1) and 4==GigG(MySet, maxnum-1))	or (2==GigG(MySet, maxnum-1) and 4==SmallG(MySet, maxnum-1)):
		MySet = [allBols[randint(0,len(allBols)-1)] for x in range(countnum)]
	# Фиксированный набор игрока
	#MySet = [1, 11, 23, 33, 41, 24]
	#MySet.sort()

	# Подсчет выпавших комбинация	
	counterwiner[int(len(set(MySet) - set(GameSet)))] +=1 #Подсчет количества совпавших комбинаций
	loglevel(level)	# Записываем в файл результат
	if counterwiner[0] > 0: break #Прекращаем игру когда выпало максимальное число совпадений		
	if count % diver == 0:# Отображаем игру кратную diver
		showresult(1)
	count += 1
	GameSet = []
	
showresult(0)
showstatistic()
