# n1, n2 = input('>').split()
# n1, n2 = int(n1), int(n2)
# print(n1+n2)
# сделать одной строкой
# print(n := 345, n//10, n % 10)
print(next(n := map(int, input('>').split())) + next(n))

# ИЛИ
n = map(int, input('>').split())
print(next(n) + next(n))