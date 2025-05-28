# Створити# клас# Rectangle:# -віy # має# приймати# дві# сторони# x, y
# Описати# поведінку# арифметичним# методом:# #
# + сума# площин# двох# екземплярів# класу# #
# – різниця# площин# двох# екземплярів# класу
# # == площин# на# рівність#
# != площин# на# нерівність
# # >, < менше# більше
# # при# виклику# метода# len()# підраховувати# суму# сторін
#
from abc import abstractmethod
from itertools import count
from typing import Self
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def add_area(self, other: Self):
        return self.area + other.area

    def difference_area(self, other: Self):
        return self.area - other.area

    def equality_area(self, other: Self):
        return self.area == other.area

    def no_equality_area(self, other: Self):
        return self.area != other.area

    def less_then_other_area(self, other: Self):
        return self.area < other.area

    def greater_then_other_area(self, other: Self):
        return self.area > other.area

    def len(self):
        return self.x + self.y

rectangle1 = Rectangle(2, 3)
rectangle2 = Rectangle(3, 4)

print(rectangle1.area)
print(rectangle2.area)
print(rectangle1.add_area(rectangle2))
print(rectangle1.difference_area(rectangle2))
print(rectangle2.difference_area(rectangle1))
print(rectangle1.equality_area(rectangle2))
print(rectangle1.no_equality_area(rectangle2))
print(rectangle1.less_then_other_area(rectangle2))
print(rectangle1.greater_then_other_area(rectangle2))
print(rectangle1.len())
print(rectangle2.len())


# ###############################################################################
# #
# створити# клас# Human(name, age)
# # створити# два# класи# Prince# и# Cinderella, які# наслідуються# від# Human:# # у
# попелюшки# має# бути# ім’я, вік, розмір# ноги# # у# принца# має# бути# ім’я, вік, та# розмір# знайденого
# черевичка, а# також# метод, котрий# буде# приймати розмір
# попелюшок, та# шукати# ту# саму
## в# класі# попелюшки# має# бути# count, який# буде# зберігати# кількість# створених# екземплярів
# класу
# # також# має# бути# метод# класу, який# буде# виводити# це# значення
#

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    __count = 0
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size
        Cinderella.__count += 1
    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        print(cls.__count)


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def search_shoe (self, princesses: list[Cinderella]):
        for cinderella in princesses:
            if cinderella.size == self.shoe_size:

                print(f'{self.name} married with {cinderella.name}')




princesses: list[Cinderella] = [
    Cinderella('Olena', 23, 36),
    Cinderella('Maria', 21, 37),
    Cinderella('Oksana', 24, 39),
    Cinderella('Iryna', 26, 38),
    Cinderella('Ania', 28, 36),
    Cinderella('Oksana', 23, 38),
    Cinderella('Kateryna', 27, 37)

]

prince = Prince('Andrii', 30, 39)

prince.search_shoe(princesses)
Cinderella.get_count()



# ###############################################################################
#
#
# 1) Створити# абстрактний# клас# Printable, який# буде# описувати# абстрактний# метод# print()
#
# 2) Створити# класи# Book# та# Magazine, в# кожного# в# конструкторі# змінна# name, та
# який# наслідується# від# класу Printable
#
# 3) Створити# клас# Main, в# якому# буде:#
# – змінна# класу# printable_list, яка# буде# зберігати# книжки# та# журнали#
# – метод# add, за# допомогою# якого# можна# додавати екземпляри# класів# в# список# і
# робити# перевірку, чи# то, що# передають, є# класом# Book# або# Magazine# інакше# ігнорувати# додавання
#
# – метод# show_all_magazines, який# буде# виводити# всі# журнали, викликаючи# метод# print# абстрактного# класу
#
# – метод# show_all_books, який# буде# виводити# всі# книги, викликаючи# метод# print# абстрактного
# класу
#



from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'BOOK: {self.name}')

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'MAGAZINE: {self.name}')

class Main:
    __printable_list: list[Printable] = []
    @classmethod
    def add__(cls, item):
        if isinstance (item, Book or Magazine):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()




Main.add__(Book('Book1'))
Main.add__(Book('Book2'))
Main.add__(Magazine('Magazine1'))
Main.add__(Magazine('Magazine2'))
Main.add__(Magazine('Magazine3'))
Main.show_all_books()
print('-' *40)
Main.show_all_magazines()


# Приклад:
#
# Main.add(Magazine(‘Magazine1’))
#
# Main.add(Book(‘Book1’))
#
# Main.add(Magazine(‘Magazine3’))
#
# Main.add(Magazine(‘Magazine2’))
#
# Main.add(Book(‘Book2’))
#
#
#
# Main.show_all_magazines()
#
# print(‘-‘ *40)
#
# Main.show_all_books()
#
# для# перевірки# класів# використовуємо# метод# isinstance, приклад:
#
# user = User(‘Max’, 15)
#
# shape = Shape()
#
# isinstance(max, User) -> True
#
# isinstance(shape, User) -> False
#
