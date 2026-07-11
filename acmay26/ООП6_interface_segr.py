from abc import ABC, abstractmethod


class Gadget(ABC):

    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def inet(self):
        pass

    @abstractmethod
    def video(self):
        pass


# class SmartPhone(Gadget) #
#
#     def talk(self):
#         print('Обеспечивает разговор')
#
#     def inet(self):
#         print('Обеспечивает internet')
#
#     def video(self):
#         print('Обеспечивает video')
#
#
# class Telephone(Gadget): # это не удобно, тк эти методы не подходят но мы обязаны прописать, используем второй вариант
#
#     def talk(self):
#         print('Обеспечивает разговор')
#
#     def inet(self):
#         pass
#
#     def video(self):
#         pass
#---------------------------------------------------------
# разделение
class Talk(ABC):
    @abstractmethod
    def talk(self):
        pass


class Video(ABC):
    @abstractmethod
    def video(self):
        pass


class Inet(ABC):
    @abstractmethod
    def inet(self):
        pass


class SmartPhone(Talk, Inet, Video):
    def talk(self):
        print('Обеспечивает разговор')

    def inet(self):
        print('Обеспечивает internet')

    def video(self):
        print('Обеспечивает video')


class Telephone(Talk):
    def talk(self):
        print('Обеспечивает разговор')