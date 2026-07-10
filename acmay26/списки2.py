"""list"""
#
# people = [['Mary', 26], ['Frol', 18], ['John', 19], ['Alex', 36]]
# people.sort(key=lambda x: x[1])
# # print(people)
#
# nums = [22, 33, 55, 44, 99]
# names = ['Mary', 'Berry', 'Terry', 'Dasha', 'Sasha']
# dates = [12, 13, 14, 15, 16]
#
# for i in range(len(nums)):
#     print(i, nums[i], end='   ')
# print()
#
# cnt = 0
# for n in nums:
#     print(cnt, n, end='   ')
#     cnt += 1
# print()
#
# for n in enumerate(nums):
#     print(n, end='   ')
# print()
#
# for n in enumerate(nums):
#     print(n[0], n[1], end='   ')
# print()
#
# for n, m in enumerate(nums):
#     print(n, m, end='   ')
# print()
# print(list(enumerate(nums)))
# # n, m = (0, 22)
# # print(n)
# # print(type(n))
# for n, name in enumerate(names, 1):
#     print(f'{n}. {name}')
#
# for n, name, d in zip(nums, names, dates):
#     print(f'{n} : {name} : {d}')
#
# age = [22, 33, 55, 44, 19]
# names = ['Mary', 'Berry', 'Terry', 'Dasha', 'Sasha']
# nums = [12, 23, 14, 45, 16]
#
# for a, name, n in zip(age, names, nums):
#     print(f'{name} : {a} age, №{n}')
#
# people = [['Mary', 26, 120], ['Frol', 18, 110],
#           ['John', 19, 200], ['Alex', 36, 133]]
# for p in people:
#     print(p)
#     for n in p:
#         print(n)
#
# print(len(people[1]))

# Пример: заполнить список
#1 вариант
sguare = []
for i in range (10, 20):
    sguare.append(i ** 2)
print(sguare)
#2 вариант
sguare = [0] * 10
for i in range (10):
    sguare[i] = (i+10) ** 2
print(sguare)
# 3 вариант лист комп-н
sguare = [i ** 2 for i in range (10, 20)]
print(sguare)