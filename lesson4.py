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


#
# try:
#     with open('email.txt', 'w+') as file:
#         file.write('9d3dc7094d3dcb31ffe2960ad891dd04 34hrap@gmail.com\nec4f2883e9eb74770d02b30f06659a5f tele_nat@mail.i\n44ab3c993daee2a9655925d53fbdd7bf telepaev.sn@gmail.com')
# except Exception as e:
#     print(e)
#
# try:
#     with open('gmail.txt', 'w+') as file2:
#         for letter in file:
#             if letter == 'gmail.com':
#                 file2.write('gmail.com\n')
# except Exception as a:
#     print(a)
# ------------------------------------------------------------

try:
    with open('email.txt', 'w') as file1:
        file1.write('9d3dc7094d3dcb31ffe2960ad891dd04 34hrap@gmail.com\nec4f2883e9eb74770d02b30f06659a5f tele_nat@mail.i\n44ab3c993daee2a9655925d53fbdd7bf telepaev.sn@gmail.com')
except Exception as e:
    print(e)


try:
    with open('email.txt') as file1, open('gmail.txt', 'w') as file2:
        for line in file1:
            gmail = line.split()[-1]
            if gmail.endswith('gmail.com'):
                file2.write(f'{gmail}\n')
except Exception as e:
    print(e)


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
# class Products:
#
#     product_book = []
#     def __init__(self, file_book):
#         self.file_book = file_book
#
#     @classmethod
#     def add_product (self, id, name, price):
#         self.product_book.append({'id': id, 'name': name, 'price': price})
#
#
#     @classmethod
#     def search_product(self, key):
#         for product in self.product_book:
#             if key == product.name:
#                 print(product)
#             elif key == product.id:
#                 print(product)
#
#     @classmethod
#     def max_value(self):
#         print(max(self.product_book, key=lambda p: p['price']))
#
#     @classmethod
#     def __delitem__(self, index):
#         del self.product_book[index]
#
#     @classmethod
#     def menu(cls):
#         print(f'MENU:\nAdd Product:{Products.add_product()} ')
# Products.add_product(1, 'Apple', 40)
# Products.add_product(2, 'Orange', 55)
# Products.add_product(3, 'Carrot', 35)
# Products.add_product(4, 'Cucumber', 45)
# Products.add_product(5, 'Potato', 30)
# Products.add_product(6, 'Banana', 65)
# print(Products.product_book)
# Products.max_value()
# Products.__delitem__(2)
# print(Products.product_book)
# print(Products.search_product(2))
# ___________________________________________________________

import json
class Products:
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.__products = []
        self.__read_file()
        self.__id = self.__gen_id()

    def shaw_all(self):
        for product in self.__products:
            print(f'{product['id']} {product['name']} - {product['price']} UAH')

    def add(self):
        name = input('Enter product name: ')
        while True:
            try:
                price = float(input('Enter product price: '))
                break
            except ValueError:
                pass
        new_products = {'id': next(self.__id), 'name': name, 'price': price}
        self.__products.append(new_products)
        self.write_file()

    def write_file(self):
        try:
            with open(self.file_name, mode='w') as file1:
                json.dump(self.__products, file1)
        except Exception as r:
            print(r)

    def __read_file(self):
        try:
            with open (self.file_name, mode='r') as file2:
                self.__products = json.load(file2)
        except (Exception, ):
            self.__products = []

    def __gen_id(self):
        _id = self.__products[-1]['id']+1 if self.__products else 1
        while True:
            yield _id
            _id += 1

    def find_by(self):
        value = input('Enter value: ')
        for product in self.__products:
            if value in product.values() or value.isdigit() and float(value) in product.values():
                print(product)

    def most_expensive(self):
        print(max(self.__products, key=lambda x: x['price']))

    def delete_by_id(self):
        self.shaw_all()

        while True:
            try:
                _id = int(input('Enter product id: '))
                break
            except ValueError:
                pass
        index = next((i for i, v in enumerate(self.__products) if v['id'] == _id), None )\

        if index:
            del self.__products[index]
            self.write_file()
            return
        print('No such product id')

    def menu(self):
        while True:
            print('1. Show all products')
            print('2. Add product')
            print('3. Most expensive')
            print('4. Delete product by ID')
            print('5. Search for product')
            print('6. Exit')

            choice = input('Enter choice: ')
            if choice == '1':
                products.shaw_all()
            if choice == '2':
                products.add()
            if choice == '3':
                products.most_expensive()
            if choice == '4':
                products.delete_by_id()
            if choice == '5':
                products.find_by()
            if choice == '6':
                return







products = Products('products.json')
products.shaw_all()
# products.add()
products.write_file()
# products.find_by()
products.most_expensive()
# products.delete_by_id()
products.shaw_all()
products.menu()



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



data = [
    [
{'id': 1110, 'field': {}},

{'id': 1111, 'field': {}},

{'id': 1112, 'field': {}},

{'id': 1113, 'field': {}},

{'id': 1114, 'field': {}},

{'id': 1115, 'field': {}},
],

[
{'id': 1110, 'field': {}},

{'id': 1120, 'field': {}},

{'id': 1122, 'field': {}},

{'id': 1123, 'field': {}},

{'id': 1124, 'field': {}},

{'id': 1125, 'field': {}},
],

[
{'id': 1130, 'field': {}},

{'id': 1131, 'field': {}},

{'id': 1122, 'field': {}},

{'id': 1132, 'field': {}},

{'id': 1133, 'field': {}},
]

]



def cut(arr):
    res = []
    gen = [(i['id'] for i in item if i['id'] not in res) for item in arr]
    while gen:
        g = gen.pop()
        try:
            res.append(next(g))
            gen.append(g)
        except StopIteration:
            pass
    return res

print(cut(data))
