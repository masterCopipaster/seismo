from processing import *

import matplotlib.pyplot as plt 
import numpy as np

print("Скрипт производит шаги поиска отраженной волны")  
grid, s = loadcsv(input("Введите имя csv файла осцилограммы:  "))
fwidth = int(len(s) / 50)
myfigsize = (16, 8)
print('''Файл успешно загружен
сигнал помещен в переменную s
временная решетка помещена в переменную grid
ширина фильтра fwidth по умолчанию установлена в 1/50 ширины сигнала
вам показан график сигнала, чтобы начать обработку закройте окно и введите команды предобработки
например обрезка s = s[start:stop] grid = grid[start:stop]
после исполнения команд предобработки нажмите enter
''')



plt.figure(figsize = myfigsize)
plt.title("Original signal")
plt.plot(s, label = "signal")
plt.legend()
plt.grid()
plt.draw()
plt.show()

l = input("введите команды:  ")
commands = []
up_imported = False
while l != "":
    exec(l)
    if l == "import user_processing":
        up_imported = True
    else:
        commands.append(l + "\n")
    l = input()
up_file = open("user_processing.py", "a" if up_imported else "w")
up_file.writelines(commands)
up_file.close()

plt.figure(figsize = myfigsize)
plt.title("preprocessed signal ")
plt.plot(grid, s, label = "signal")
plt.legend()
plt.grid()
plt.draw()

plt.figure(figsize = myfigsize)
plt.title("Signal convolved with itself time-inverted")
aconv = np.abs(inv_conv(s))                     
plt.plot(grid, aconv, label = "inverted convolution")
plt.legend()
plt.grid()
plt.draw()

plt.figure(figsize = myfigsize)
plt.title("2nd order runmean filtering")
filtered = runmean(runmean(aconv, fwidth), fwidth) 
plt.plot(grid, filtered, label = "filtered")
#poly = np.polyfit(grid, filtered, 15)
#Spolyapp = np.polyval(poly, grid)
#plt.plot(polyapp, label = "aproximated")
plt.legend()
plt.grid()
plt.draw()

plt.figure(figsize = myfigsize)
plt.title("Time normalizing")
tgrid = np.arange(len(grid))
timenorm = filtered * tgrid
#poly = np.polyfit(grid, timenorm, 15)
#p1d = np.polyder(poly, 1)
#roots = np.roots(p1d)
#rroots = []
#for c in roots:
#    if np.imag(c)==0:
#        rroots.append(np.real(c))
#rroots = np.array(rroots)

#polyapp = np.polyval(poly, grid)
plt.plot(grid, timenorm, label = "normalized")
#plt.plot(polyapp, label = "aproximated")
#plt.plot(rroots * 10, np.polyval(poly, rroots), "r+")
plt.legend()
plt.grid()
plt.draw()

#print("real roots", rroots * 10)

plt.figure(figsize = myfigsize)
gradient = runmean(np.gradient(timenorm), fwidth)
plt.plot(grid, gradient, label = "normalised signal gradient")
plt.show()
input("press any key to exit")