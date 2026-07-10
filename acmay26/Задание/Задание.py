"""
Доработайте программу калькулятора calc_dz.py. Добавьте функцию, которая позволит пользователю
 просматривать историю всех выполненных ранее вычислений. Эта функция будет читать данные из
  файла, в который записываются результаты (calculations.txt), и выводить их пользователю.
"""
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y

def log(result):
    with open("calculations.txt", "a",encoding = 'utf-8') as file:
        file.write(result + "\n")  # добавлен перевод строки для читаемости


def show_history():
# функция читает файл ..txt и выводит сохраненные вычисления
    try: #try\except
        with open ("calculations.txt", "r", encoding = 'utf-8') as file:
            lines = file.readlines() #метод файлового объекта читает все строки из файла и возвращает
            # их в виде списка, где каждый элемент списка — это одна строка из файла,
            # lines переменная, file объект файла
            if lines:
                print("\n"  + "="*30) #делает отступ и ставит верхнюю рамку
                print("ИСТОРИЯ ВЫЧИСЛЕНИЙ".center(30))
                print("="*30 + "\n")
                # print("="*30)
                for i, line in enumerate(lines, 1):# порядковый номер с 1
                    print(f"{i}. {line.strip()}") #выводит пронумер.строку из истории вычислений
                print("="*30)#это умножение строки на число Python берёт строку "="
                # и повторяет её 30 раз подряд.
            else:
                print("\nИстория пуста.")

    except FileNotFoundError: # чтение несуществующего файла
        print("Файл не найден")
    except Exception as e:
        print(f"\nНепредвиденная ошибка:{e}") #переменная е объект ошибки


print("Выберите операцию: ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Просмотр историй вычислений")

choice = input("Введите номер операции (1/2/3/4/5): ")
if choice =='5':
    show_history()
else:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    if choice == '1':
        r = f"Результат: {num1} + {num2} = {add(num1, num2)}"
        print(r)
        log(r)
    elif choice == '2':
        r = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
        print(r)
        log(r)
    elif choice == '3':
        r = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
        print(r)
        log(r)
    elif choice == '4':
        r = f"Результат: {num1} / {num2} = {divide(num1, num2)}"
        print(r)
        log(r)
    else:
        print("Неверный ввод")