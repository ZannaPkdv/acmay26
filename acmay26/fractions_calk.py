import math
from tkinter import *


def get_items():
    try:
        err_info['text'] = ''
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())
        znak = oper.get().strip()

        if znak == '':
            raise NotImplementedError('Не задан знак операции!')
            # znak = '+'
            # oper.insert(0, '+')

        match znak:
            case '+':
                n = n1 * d2 + n2 * d1 # математическая формула сложения
                d = d1 * d2
            case '-':
                n = n1 * d2 - n2 * d1
                d = d1 * d2
            case '*':
                n = n1 * n2
                d = d1 * d2
            case '/':
                n = n1 * d2
                d = d1 * n2

        nod = math.gcd(n, d)
        n = n // nod
        d = d // nod
        int_p = ''

        if n % d == 0:
            int_p = n // d
            n = 0
            d = 0
        elif n > d:
            int_p = n // d
            n = n % d

        int_part['text'] = int_p
        num3['text'] = str(n) if n != 0 else ''
        den3['text'] = str(d) if d != 0 else ''
    except Exception as err:
        match err.__class__.__name__:
            case 'ZeroDivisionError':
                err_info['text'] = 'Ошибка! Нулевое значение \n' \
                                   'в дроби не допустимо!'
            case 'ValueError' | 'TypeError':
                err_info['text'] = 'Ошибка! Дробь должна \n' \
                                   'состоять только из цифр!'
            case 'NotImplementedError':
                err_info['text'] = 'Ошибка! Не задан знак операции!\n + , - , * или /'
            case _:
                err_info['text'] = ('Ошибка: ' + (type(err).__name__) + '\n' +
                                    str(err) + '!')

        print('Error: ', type(err).__name__, err)


root = Tk() # окно главное создание окна методом TK
root.title('Fractions calculator')
root.geometry('300x200+1100+100')
# менеджеры разметки pack(сверху снизу справо слево центр ) grid (конкретно указывает колонку и строку )

frame = Frame(root) #  в первое окно заходит второе
frame.pack(pady=10)  # в root теперь можно использовать только pack()

#Entry для того чтобы вводить значение
num1 = Entry(frame, width=2, font=('Arial', 15), justify='center') #это первый столбик  квадратик сверху
num1.grid(row=0, column=0)  # в frame теперь можно использовать только grid()
line1 = Label(frame, text=chr(9135) * 5)
line1.grid(row=1, column=0)
den1 = Entry(frame, width=2, font=('Arial', 15), justify='center') #это квадратик снизу первый столбик
den1.grid(row=2, column=0)  # в frame теперь можно использовать только grid()

oper = Entry(frame, width=2, font=('Arial', 15), justify='center')# это мы устанавливаем знак плюс минус умножение  и тд
oper.grid(row=1, column=1, padx=5)# padx=5 это отступ от столбика

num2 = Entry(frame, width=2, font=('Arial', 15), justify='center')
num2.grid(row=0, column=2)  # в frame теперь можно использовать только grid()
line2 = Label(frame, text=chr(9135) * 5)
line2.grid(row=1, column=2)
den2 = Entry(frame, width=2, font=('Arial', 15), justify='center')
den2.grid(row=2, column=2)  # в frame теперь можно использовать только grid()
# Button нажать кнопку
equal = Button(frame, text='=', width=2, height=1, command=get_items)
equal.config(font=('Arial', 15))
equal.grid(row=1, column=3, padx=5)

int_part = Label(frame, text='  ')
int_part.config(font=('Arial', 20), justify='center', bg='lightgrey', width=2)
int_part.grid(row=1, column=4)

num3 = Label(frame, width=2, font=('Arial', 15), justify='center', bg='lightgrey')
num3.grid(row=0, column=5)  # в frame теперь можно использовать только grid()
line3 = Label(frame, text=chr(9135) * 5)
line3.grid(row=1, column=5)
den3 = Label(frame, width=2, font=('Arial', 15), justify='center', bg='lightgrey')
den3.grid(row=2, column=5)  # в frame теперь можно использовать только grid()

err_info = Label(root, font=('Courier New', 10), justify='center', fg='red')
err_info.pack()

root.mainloop()
