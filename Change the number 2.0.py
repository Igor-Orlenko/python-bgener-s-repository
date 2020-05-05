import random
from tkinter import *

n = random.randint(1, 100)
u_n = 0


def new_number():
    global n
    n = random.randint(1, 100)


def get_int():
    global u_n
    u_n = u_number.get()

    if int(u_n) < n:
        res['text'] = 'Загаданное число больше'
        u_number.delete(0, END)
    elif int(u_n) > n:
        res['text'] = 'Загаданное число меньше'
        u_number.delete(0, END)
    else:
        res['text'] = 'Вы угадали число, для продолжения или остановки сессии используйте кнопи сверху.'
        u_number.delete(0, END)


def stop_s():
    res['text'] = 'Спасибо за игру'
    exit()


root = Tk()
root.geometry('600x400+1000+300')

new = Button(root, text='Начать новую игру', command=new_number).pack()
stop = Button(root, text='Остановить сессию', command=stop_s).pack()

gate = Label(root, text='Число загадано, введите ваше предположение.')
gate.pack()

u_number = Entry(root)
u_number.pack()

gn = Button(root, text='ввести догадку', command=get_int)
gn.pack()

res = Label(root)
res.pack()
root.mainloop()
