from time import sleep
from random import randint
import time
lud = randint(50,500)
ud = 0
kz = 0 #Численость землекрушений
kc = 0 #Численость очишеных
kp = 0 #Численость спасёных
kb = 0
slud = 0 #Спавн людей
ub = 0
print(f' Хозяин у нас {lud} людей')
print("Что будем делать с ними?")

save = open('save.txt','r')
f = save.readline()
print(f)
save.close()

def clear():
        global ud
        global lud
        global kc
        global ub
        print("Сейчас будет проведена отчистка от грешников")
        time.sleep(5)
        ud = randint(25,100)
        lud = lud - ud
        print(f"Осталось {lud} чистых душ")
        kc = kc + ud
        ub = ub + ud
def zem():
        global kz
        global ud
        global lud
        global ub
        print("Сейчас будет землетресение")
        time.sleep(5)
        ud = randint(100,200)
        lud = lud - ud
        kz = kz + 1
        ub = ub + ud
        print(f"Осталось {lud} чистых душ")
def moneta():
        global lud
        global ud
        global ub
        ub = ub + lud // 2
        print("Сейчас будет очишено 50% населения")
        time.sleep(10)
        lud = lud // 2
        print("Очистка завершена")
def spawn():
        global lud
        global slud
        slud = int(input("Сколько людей будет заспавлено?"))
        lud = lud + slud
def pros():
        global kp
        global ud
        global lud
        pros = randint(1, ud)
        lud = lud + pros
        print(f'Вы воскресили {pros} людей')
        kp = kp + pros
def info():
        global ud
        global lud
        print("осталось", lud, "Было убито", ub, "Воскрешено было",kp )
def bog():
        global lud
        global ub
        global kb
        print("Бог возратил всех умерших")
        time.sleep(30)
        lud = lud + ub
        kb = kb + 1
        print("Все мёртвые стали жить")
while True:
    command = input()
    if command == "clear":
        clear()
    if command == "zem":
        zem()
    if command == "info":
        info()
    if command == "pros":
        pros()
    if command == "moneta":
        moneta()
    if command == "spawn":
        spawn()
    if command == "bog":
        bog()
    if lud <= 0:
        print(kz,"Землетресений было", kc,"очишеных было", kp, "Прошёных было", kb,"раз был вызван бог")
        break
    if command == 'stop':
        break
