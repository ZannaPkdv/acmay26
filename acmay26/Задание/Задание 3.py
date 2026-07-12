from tkinter import *
from tkinter import messagebox as mb

def summ_three():
    # s1 = e1.get()
    # s2 = e2.get()  #е1 это поле ввода а get берет оттуда все что напечатали и возвращает как строку в переменную s1
    # s3 = e3.get()
    #
    #ЭТО БЫЛО В ЗАДАНИЕ
    # if not s1.lstrip('-').isdigit():
    #     mb.showerror("Ошибка", "В первое поле должно быть введено число")
    #     return
    # s2 = e2.get()
    # if not s2.lstrip('-').isdigit():
    #     mb.showerror("Ошибка", "Во второе поле должно быть введено число")
    #     return
    # s3 = e3.get()
    # if not s3.lstrip('-').isdigit():
    #     mb.showerror("Ошибка", "В третье поле должно быть введено число")
    #     return

    try:
        n1 = float(e1.get())
    except ValueError:
        mb.showerror("Ошибка""В первое поле должно быть введено корректное число")
    try:
        n2 = float(e2.get())
    except ValueError:
        mb.showerror("Ошибка""Во второе поле должно быть введено корректное число")
    try:
        n3 = float(e3.get())
    except ValueError:
        mb.showerror("Ошибка""В третье поле должно быть введено корректное число")



    # num1 = int(s1)
    # num2 = int(s2)
    # num3 = int(s3)
    result = n1 + n2 + n3
    m1['text'] = f"{n1} + {n2} + {n3} = {round(result, 2)}"  #round -округление

    answer = mb.askretrycancel(title="Вопрос", message="Сложить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()


def multi_three():
    # s1 = e1.get()
    # s2 = e2.get()
    # s3 = e3.get()
    try:
        n1 = float(e1.get())
    except ValueError:
        mb.showerror("Ошибка""В первое поле должно быть введено корректное число")
    try:
        n2 = float(e2.get())
    except ValueError:
        mb.showerror("Ошибка""Во второе поле должно быть введено корректное число")
    try:
        n3 = float(e3.get())
    except ValueError:
        mb.showerror("Ошибка""В третье поле должно быть введено корректное число")
#  ЭТО БЫЛО В ЗАДАНИЕ
    # if not s1.lstrip('-').isdigit():
    #     mb.showerror("Ошибка", "В первое поле должно быть введено число")
    #     return
    # s2 = e2.get()
    # if not s2.lstrip('-').isdigit():
    #     mb.showerror("Ошибка", "Во второе поле должно быть введено число")
    #     return
    # s3 = e3.get()
    # if not s3.lstrip('-').isdigit():
    #     mb.showerror("Ошибка", "В третье поле должно быть введено число")
    #     return
    #
    # num1 = int(s1)
    # num2 = int(s2)
    # num3 = int(s3)
    result = n1 * n2 * n3
    #m1['text'] = f"{s1} * {s2} * {s3} = {str(result)}"
    m1['text'] = f"{n1} * {n2} * {n3} = {round(result, 2)}"

    answer = mb.askretrycancel(title="Вопрос", message="Умножить еще три числа?")# способ спросить пользователя
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

window = Tk()
window.title("Калькулятор")

m = Label(height=3, text="Введи три числа и выбери действие")# устанавливает текст
m.pack()

e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()
e3.pack()

b = Button(text="Сложить три числа", command=summ_three) #создаем кнопку при нажатии вызывает функцию
b.pack()
b1 = Button(text="Умножить три числа", command=multi_three)
b1.pack()# разместить табличку в окне
m1 = Label(height=3)
m1.pack()

window.mainloop()