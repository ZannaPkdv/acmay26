import matplotlib. pyplot as plt

# def summator(*v):
#     x = 0
#     y = 0
#     for k, vy, in v:
#         x += k
#         y += vy
#     return x, y
# v1 = (10,20)
# v2 = (10,2)
# v = v1 + v2
# print(v)
# print(type(v))
# v = summator(v1,v2)
# print(v)

# Создаем свой класс
#классы строятся на функциях

# class Vector(object): можно и так и так написать
class Vector:
    def __init__ (self, x, y):#имя объекта класса и его значение  v1 это seif
        self.x = x
        self.y = y
        # self.cnt =


    def __add__ (self, other): # показывает как сложить
        x = self.x + other.x
        y = self.y + other.y
        return Vector (x, y)


    def display_add(self, other):
        res = self + other
        v1x = (0, self.x)
        v1y = (0, self.y)
        v2x = (0, other.x)
        v2y = (0, other.y)
        rx = [0, res.x]
        ry = [0, res.y]
        plt.plot(v1x, v1y, v2x, v2y, rx, ry, '-.', lw=3)
        plt.show()


    def __str__ (self): # метод обеспечивает что будет показывать print тк он не знает как выводить объект класс
        return f'V({self.x}, {self.y})'

v1=Vector(10, 20)
v2=Vector(10, 2)
v3=Vector(5, 5)
# print(v1.x, v1.y)
print(v1, v2)
v = v1 + v2 + v3
print(v)
v1.display_add(v2)
