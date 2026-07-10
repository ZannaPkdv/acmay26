"""tuple""" # упорядоченный набор неизменяемых объектов

# tp = (33, 'Vasiliy', True, [1, 2])
tp = (33, 'Vasiliy', True, (1, 2))
tp1 = tp[:3]
# tp[-1][0] = 10
print(tp1)
print(tp)
# tp1 = tp.copy()  # нельзя
for i in tp:
    print(i)

PI = 3.1415926,
print(PI)
print(PI[0])

tp = ('login', 'password')
print(id(tp))
buf = list(tp)
buf[-1] = 'new_password'
tp = tuple(buf)
print(tp)
print(id(tp))
tp_sort = sorted(tp, reverse=True)
print(tp_sort)
print()
