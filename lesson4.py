from operator import contains

# 1) Створити файл email.txt та наповнити його інформацію наступного формату (використайте для цього ШІ).
#
# 9d3dc7094d3dcb31ffe2960ad891dd04 34hrap@gmail.com
#
# ec4f2883e9eb74770d02b30f06659a5f tele_nat@mail.i
#
# 44ab3c993daee2a9655925d53fbdd7bf telepaev.sn@gmail.com
#
# ….
# ваша задача:  записати в новий файл тільки email’ /-ли з доменом gmail.com



try:
    with open('email.txt', 'w+') as file:
        file.write('9d3dc7094d3dcb31ffe2960ad891dd04 34hrap@gmail.com\nec4f2883e9eb74770d02b30f06659a5f tele_nat@mail.i\n44ab3c993daee2a9655925d53fbdd7bf telepaev.sn@gmail.com')
except Exception as e:
    print(e)

try:
    with open('gmail.txt', 'w+') as file2:
        for letter in file:
            if letter == 'gmail.com':
                file2.write('gmail.com\n')
except Exception as a:
    print(a)


# 2) Створити# записну# книжку# покупок:# – у
# покупки# повинна# бути# id, назва# і# ціна# # – всі# покупки# зберігаємо# в# файлі#
# з# функціоналу:#
# *вивід# всіх# покупок# #
# * має# бути# змога# додавати# покупку# в# книгу

# * має# бути# змога# шукати# по# будь - якому# полю# покупку

# * має# бути# змога# показати# найдорожчу# покупку

# * має# бути# можливість# видаляти# покупку# по# id# # (ну# і
# меню# на# це# все)
from abc import ABC, abstractmethod
from typing import Self
class Products:

    product_book = []
    def __init__(self, file_book):
        self.file_book = file_book

    @classmethod
    def add_product (self, id, name, price):
        self.product_book.append({'id': id, 'name': name, 'price': price})


    @classmethod
    def search_product(self, key):
        for product in self.product_book:
            if key == product.name:
                print(product)
            elif key == product.id:
                print(product)

    @classmethod
    def max_value(self):
        print(max(self.product_book, key=lambda p: p['price']))

    @classmethod
    def __delitem__(self):
        for item in self.product_book:
            if item == self.product_book[id]:
                del self.product_book[id]

Products.add_product(1, 'Apple', 40)
Products.add_product(2, 'Orange', 55)
Products.add_product(3, 'Carrot', 35)
Products.add_product(4, 'Cucumber', 45)
Products.add_product(5, 'Potato', 30)
Products.add_product(6, 'Banana', 65)
print(Products.product_book)
Products.max_value()
# Products.__delitem__(2)
print(Products.product_book)
# Products.__delitem__(3)
print(Products.search_product(2))











#
# ** ** ** ** *Кому# буде# замало? ось# завдання# зі# співбесіди
#
# Є# ось# такий# список:#
# data = [
#     [
# {“id”: 1110, “field”: {}},
#
# {“id”: 1111, “field”: {}},
#
# {“id”: 1112, “field”: {}},
#
# {“id”: 1113, “field”: {}},
#
# {“id”: 1114, “field”: {}},
#
# {“id”: 1115, “field”: {}},
# ],
#
# [
# {“id”: 1110, “field”: {}},
#
# {“id”: 1120, “field”: {}},
#
# {“id”: 1122, “field”: {}},
#
# {“id”: 1123, “field”: {}},
#
# {“id”: 1124, “field”: {}},
#
# {“id”: 1125, “field”: {}},
# ],
#
# [
# {“id”: 1130, “field”: {}},
#
# {“id”: 1131, “field”: {}},
#
# {“id”: 1122, “field”: {}},
#
# {“id”: 1132, “field”: {}},
#
# {“id”: 1133, “field”: {}},
# ]
#
# ]
#
#
#
# потрібно#брати# по# черзі# з# кожного# списку# id# і# класти# в# список# res.Якщо# таке# значення
# вже# є# в# результуючому# списку, то# брати# наступне# з# того# ж# підсписку
# # з# даним# списком# має# вийти# ось# такий# результат:
#
# res = [1110, 1120, 1130, 1111, 1122, …….]