s = 'ЗдравстВуйте,    гоСти! \n    darling'
s1 = '12345'

# print(s.islower())
# print(s.isupper())
# print(s.isalpha())
# print(s.isdigit())
# print(s.isnumeric())
# print(s.isalnum())
# print(s.startswith('Зд'))
# print(s.endswith('Зд'))

# print(s.lower())
# print(s.upper())
# # s = s.upper()
# print(s.capitalize())
# print(s.title())
# print(s.rjust(40))
# print(s.ljust(40))
# print(s.center(40))
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s)
# print(s.strip('! З'))
# print(s.index('т', 12))
# print(s.find('т', 12, 18))

# name = 'Andrey'
# symbol = input('Введите символ: ')
# ind = name.find(symbol)
# if ind != -1:
#     print(f'есть буква {symbol} в этом слове! index {ind}')
# else:
#     print(None)

# print(s.replace('т', 'Т'))  # O(n) - линейная
# print(s.replace(',', ''))
# print(s.replace('т', 'Т').replace('-', ''))
# res = s.replace(',', '')
# print(res)
# print(type(res))
# ls = s.split()
# print(ls)
# print(' '.join(ls))

# print(ls[1].split())
#
# sl =[ls[0]] + ls[1].split()
# print(sl)
# print(', '.join(sl))
s = 'ЗдравстВуйте, гоСти!'
res = s[11]
res = s[1:12]
res = s[::-1]  # Start:Stop:Step = 1
# print(res)


# s1 = 'казак'
# if s1 == s1[::-1]:
#     print('Palindrom')
# else:
#     print('NO')

# print(len(s))
# print(s.count('т'))

# s1 = 'aaa bbb ccc ddd eee '
# s2 = '111 222 333 444 555 '
# 'aaa 111 bbb 222 ccc 333 ddd 444 '
# res = ''
# for i in range(0, len(s1), 4):
#     res += s1[i:i + 4] + s2[i:i + 4]
# print(res)
# print(ord('G'), chr(71))
# print()
# print(chr(2926))

# s1 = input('Word: ').strip()
# # res = 'Palindrom' if s1 == s1[::-1] else None if s1[0] == 'k' else 'NO'
# res = 'Palindrom' if s1.lower() == s1[::-1].lower() else 'NO'
# print(res)
# print(s1)
# print('Vasya' + chr(32) + 'Olya')
# s1 = 'kazaK'
# s2 = s1[::-1]  # Kazak
# print(s1.lower() == s2.lower())

s = '-14x^2+12x-3=0'
# d = b^2 - 4ac
ind = s.find('x')
if ind == 0 and s[0] != '-':
    a = 1
elif s[0] == '-' and s[1] == 'x':
    a = -1
else:
    a = int(s[:ind])
print(a)
# ind1 = s.find('x', ind + 1)
s = s[ind+3:]
ind = s.find('x')
if  ind == 1 and s[0] == '+':
    b = 1
elif s[0] == '-' and s[1] == 'x':
    b = -1
else:
    b = int(s[:ind])
print(b)
