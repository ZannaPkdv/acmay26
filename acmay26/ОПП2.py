#  создаем класс разных людей
class People:
    def __init__(self, name, age):
        self.__name = name # __ это мы закрыли доступ
        self.__age = age
        self.__children = []
        self.__parent = None

    # def get_name (self): позволяет получить данные
    #     return self.__name
    #
    #
    # def set_name (self, name): устанавливает
    #     self.__name = name
    # name=property(get_name, set_name) это свойства доступа к закрытым атрибутам класса

    @property
    def name (self): # та же запись только через декораторы
        return self.__name
    @name.setter
    def name (self, name):
        self.__name = name

p1 = People ('Ольга Воробьева', 33) # объект класса р1 мы не должны иметь прямого доступа
# к объектам класса только через методы (поля и методы это атрибуты класса )
# print(p1.get_name()) получает данные
# p1.set_name('Jhoney')
# print(p1.get_name())
p1.name = 'Ольга Воробьева'
print(p1.name)