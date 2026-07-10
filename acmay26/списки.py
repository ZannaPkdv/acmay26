"""list - упорядоченный набор объектов"""
import copy

"""    0   1   2   3   4    """
ls = [22, 33, 44, 55, 99]
"""   -5  -4  -3  -2  -1  """
#
# print(ls[4])
# print(ls[-1])
# print(id(ls))
# # l1 = ls[:]
# l1 = ls.copy()
# print(id(l1))
# ls[1] = 333
# print(ls)
# print(l1)
# # l = [2, '3', [22, 23]]
# # # l1 = l.copy()
# # l1 = copy.deepcopy(l)
# # l[0] = 200
# # l[-1][0] = 220
# # print(l)
# # print(l1)
# print(ls[:3])
# ls[1] = 33
# print(ls[1:])
ls = [33, 22, 55, 44, 99]
print(ls[2:])
# print(ls[2::-1])
# new = ls[::-1]
# print(new)
# ls[1:3] = 200, 300
print(ls)

ls.append(100)  # добавить в конец списка O(1)
print(ls)
ls.insert(3, 200)  # вставить по индексу O(n)
print(ls)
print(id(ls))
ls.extend([100, 2])
# ls += [1, 2]
# ls = ls + [1, 2]
print(id(ls))

print(ls)
n = ls.pop()
nn = ls.pop(3)
print(n, nn)
# while 100 in ls:
#     ls.remove(100)
print(ls)
# x = 7
#
# y = 7
# print(x == y)

print(ls.index(100, 6, 7))
# print(ls.index(101))
ls = [33, 22, 55, 44, 99]
ls.append(100)
ls.extend([100, 2])
print(ls.count(100))
print(ls)
ls.reverse()
print(ls)
ls.sort(reverse=True)
print(ls)