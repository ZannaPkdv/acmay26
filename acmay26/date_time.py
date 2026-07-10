from datetime import datetime, date, timedelta, time, UTC

t = time(12)
# t = time(25) # ошибка hour must be in 0..23
print(t)
t = time(12, 30)
print(t)
t = time(12, 30, 15)
print(t)

d = date(2020, 12, 31) # соблюдаем формат yy mm dd
print(d.strftime("%d.%m.%y"))

dd = date.today()
print(dd)
# dt = dd + time - нельзя складывать разные типы данных
dt = datetime.today()
print(dt)
dt = datetime.combine(dd, t) # вывести в формате со временем
print(dt)

print(dd - d) # формат timedelta разница дат

current_date = datetime.now() # получаем текущее время и дату
print(current_date)

# inp_date = input('Введите дату (дд.мм.гггг): ')  # строка
# dt = datetime.strptime(inp_date, '%d.%m.%Y') # конвертируем строку в date time по шаблону
# print(dt)
# print(current_date - dt)
# print((current_date - dt).days, ' дня') # разница дат в количестве дней integer
# print(type((current_date - dt).days), ' формат') # разница дат в количестве дней integer
#
curr_date_str = datetime.now().strftime('%d.%m.%Y') ## преобразуем date time в строку по формату
print(curr_date_str)

# print(datetime.strptime('12/03/1948 16:44', '%d/%m/%Y %H:%M'))
#
# print(current_date.strftime('%A %d %B %Y %I:%M %p '))
# print(current_date.strftime('%A %d %B %Y %H:%M:%S '))
print(current_date.strftime('%A %d %B %Y %H:%M:%S.%f '))
print(current_date.strftime('%A %d %B %Y %H:%M:%S.%f')[:-3]) # из микросекунд выводит
                                                            # последние три цифры(миллисекунды)
# print(current_date.strftime('%A %d %B %Y %X'))
# print(current_date.strftime('%A %d %B %y %x'))

print(current_date.replace(year=2033))
print(current_date.replace(year=2033, microsecond=0))

print(datetime.today())
# print(datetime.utcnow()) # устаревшая форма получения мирового времени
print(datetime.now(UTC)) # новая форма получения мирового времени, надо импортировать UTC

tt = current_date.timetuple() # Текущую дату в кортеж
print(tt)
for i in tt:
    print(i)

print(current_date.weekday()) # нумерация (индексы) дней недели начинается с 0
print(current_date.isoweekday()) # нумерация как положено начинается с 1
print(current_date.isocalendar()) # получаем год, неделя месяца, день недели
print(current_date.isocalendar().week) # получаем отдельно неделю месяца

days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
print(days_of_week[current_date.weekday()]) # демонстрация для чего индексация дн.нед. с 0
print(current_date.month) # нумерация месяцев начинается с 1
months = ['', 'Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль']
print(months[current_date.month]) # первый пустой, чтобы к индексу не надо было + 1

## Расчет дней до ДР
birthdate = input('Введите дату рождения (дд.мм.гггг): ')
birthdate = datetime.strptime(birthdate, '%d.%m.%Y').date() # конвертируем
                    # строку в date time по шаблону и вытаскиваем только date дату
current_date = date.today()
c_year = current_date.year # из текущей даты получаем значение Год
birthday = birthdate.replace(year=c_year) # Заменяем год на текущий, запоминаем в др.birthday
if current_date > birthday:
    birthday = birthday.replace(year=c_year + 1) # Увеличиваем год на 1, если ДР уже был в этом году
elif current_date == birthday:
    print(f'Поздравляем с днём рождения!')
    exit(0) # Завершаем программу с кодом 0 - успешное завершение
amount_days = (birthday - current_date)
eday = amount_days.days % 10 # получаем из кол-ва дней единицы
print(eday) # в строке с переносом \ нельзя писать комментарий
                                                    # Пример использования тернарного if:
print(f'До дня рождения осталось {amount_days.days}\
 {'день' if eday == 1 else 'дней' if eday > 4 else 'дня'}') # в f-строке. Если заканчивается
                                                        # на 1 - печатаем "день"
                                                 # если более чем на 4 -  "дней"
                                                 # в остальных случаях -   "дня"
                                                 # не учтен случай с 0 -  СРС)))


