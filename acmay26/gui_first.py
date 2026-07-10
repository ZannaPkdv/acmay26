from tkinter import *
from time import strftime
from tkinter import messagebox
import pygame as pg


def start():
    global alarm_time
    alarm_time = alarm.get().strip()  # считываем символы из Еntry alarm
    messagebox.showinfo('Предупреждение',
                        f'Будильник установлен на {alarm_time}')

#
def stop():
    global alarm_time
    alarm_time = ''
    alarm.delete(0, END) # после выключить время стерто
    pg.mixer.music.stop() # отключить музыку
    messagebox.showinfo('Предупреждение', "Будильник отключён")

#
def tick():
    global alarm_time
    curr_time = strftime('%H:%M:%S')  # получаем текущее время в строковом формате
    if alarm_time == curr_time: # время будильника совпадает с текущем временем
        alarm_time = ''
        pg.mixer.music.play() # включить музыку
    current_time.config(text=curr_time)  # меняем значение Label на текущее время
    current_time.after(1000, tick)  # вызов tick один раз в секунду, чтобы часы тикали-работали

pg.mixer.init()  # подключаю pygame
pg.mixer.music.load('music.mp3') # загрузка мелодии
pg.mixer.music.set_volume(.5) # установка громкости музыки

root = Tk()  # создаем объект 'окно'
WIDTH = root.winfo_screenwidth()  # получаем ширину монитора в пикселях
HEIGHT = root.winfo_screenheight()  # получаем высоту монитора в пикселях
# print(WIDTH, HEIGHT)
X = 450  # задаем ширину окна root
Y = 250  # задаем высоту окна root
# # root.geometry('450x250+400+200')# размер окна root + смещение его на экране
root.geometry(f'{X}x{Y}+{WIDTH // 2 - X // 2 + 400}+'
              f'{HEIGHT // 2 - Y // 2 - 20 - 200}') # адаптивное размещение окна root
# # в центре экрана на любом мониторе
root.title('Будильник')
root.config(bg='black')
#
current_time = Label(root, text='00:00:00')
current_time.config(font=('Arial', 50), fg='lime', bg='black')
current_time.pack()  # side=LEFT( RIGHT, BOTTOM, TOP)
#
alarm = Entry(root)# окно для установки времени звонка
alarm.config(width=10, justify='center', font=('Arial', 20))
alarm.pack()
#
start_btn = Button(root) # кнопка включения
start_btn.config(width=10, text='Включить', justify='center',
                 font=('Arial', 10), command=start)
start_btn.pack(pady=10) # отступ он кнопки снизу -вверх

stop_btn = Button(root)# ryjgrf dsrk.xtybz
stop_btn.config(width=10, text='Выключить', justify='center',
                font=('Arial', 10), command=stop)
stop_btn.pack()
alarm_time = ''# глобальная переменная
#
tick()
root.mainloop()