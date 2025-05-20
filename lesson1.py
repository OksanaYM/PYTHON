# 1) написати прогу, яка вибирає зі# введеної# строки# цифри# і# виводить
# їх# через# кому,# наприклад:# st = ‘ as 23 fdfdg544’ введена
# строка
#
# 2, 3, 5, 4, 4  # вивело в консолі.
from dataclasses import replace

st = ' as 23 fdfdg544'
print(', '.join(num for num in st if num.isdigit()))


#################################################################################
#
# 2)написати# прогу, яка# вибирає# зі# введеної# строки
# числа# і# виводить# їх# так, як# вони# написані# наприклад:
## st = ‘ as 23 fdfdg544 34’  # введена строка
#
st = ' as 23 fdfdg544'
print(', '.join(''.join(num2 if num2.isdigit() else ' ' for num2 in st).split()))

# 23, 544, 34  # вивело в консолі
#
# #################################################################################
#
#
# list
# comprehension
#
# 1) є
# строка:
#
# greeting = ‘Hello, world’
#
# записати кожний# символ, як# окремий# елемент
# списку, і# зробити# його# заглавним:
#
# [‘H’, ‘E’, ‘L’, ‘L’, ‘O’, ‘, ’, ‘ ‘, ‘W’, ‘O’, ‘R’, ‘L’, ‘D’]

greeting = 'Hello, world'

print(list((greeting ).upper()))


# 2) з# діапазону# від# 0 - 50# записати# тільки# непарні# числа, при
# цьому# піднести# їх# до# квадрату# приклад:

print([i**2 for i in range(50) if i % 2 ==1])

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, …]
#
#
# function
#
#
#
# – створити# функцію, яка# виводить
# List
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

def show_list(list) :
    for i in list:
        print(i)

show_list(list)

#
# – створити# функцію, яка# приймає# три# числа, та# виводить
# та# повертає# найбільше.
def num (num1, num2, num3 ) :
    print(max(num1, num2, num3))
num(100, 300, 200)

def show_max(num1, num2, num3) :
    res = max(num1, num2, num3)
    print(res)
    return res
show_max(10, 20, 30)


# – створити# функцію, яка# приймає# будь - яку# кількість
# чисел, повертає# найменше, а# виводить# найбільше
def find_min_max_in_list (numbers_list):
    min_value = 0
    max_value = 0
    for num in numbers_list:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    print(max_value)
    return min_value
find_min_max_in_list([6, 10, 7, 8 , 9])


def min_max (*args):
    print(max(args))
    return min(args)
min_max( 33, 44, 55, 77, 88)

# – створити# функцію, яка# повертає# найбільше# число# з
# List
#
def max_num (list):
    print(max(list))
    return max(list)
max_num([111, 333, 444, 555])



# – створити функцію, яка# повертає# найменше# число# з# List
#
def min_num (list):
    print(min(list))
    return min(list)
min_num([111, 333, 444, 555])

# – створити# функцію, яка# приймає# List# чисел
# та# складає# значення# елементів# List# та# повертає# його.
#
def sum_num (list_num):
    print (sum(list_num))
    return sum(list_num)
sum_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# – створити# функцію, яка# приймає# List# чисел та# повертає# середнє
# арифметичне його# значень.
#
def avar_value (list):
    res = ((sum(list))/len(list))
    print(res)
    return res
avar_value([1, 2, 3, 4, 5])


# Є# list:
#
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# – знайти# мін.число
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
print(min(list))
# – видалити# усі# дублікати
#
print(set(list))

# – замінити# кожне# 4 - те# значення# на ‘X’
#
def to_x():
    copy_list = list.copy()
    print(['X' if not (i+1)%4 else item for i, item in enumerate (copy_list)])
to_x()

# 2) вивести# на# екран# пустий# квадрат# з “ * ”, сторона
# якого# вказана# як# аргумент# функції

def quadra_def (num) :
    for i in range(num):
        if i == 0 or i == num-1:
            print (num * '*')
        else:
            print('*' + ((num-2)*' ' + '*'))

quadra_def(5)


# 3) вивести# табличку# множення
# за# допомогою# циклу# while
#

def multi_table  ():
    num = 9
    item1 = 1
    while item1 <= num :
        item2 = 1
        while item2 <= num :
            res = item1 * item2
            print(' ' if res//10 else '  ', end='')
            print(res, end= '')
            item2 += 1
        print ()
        item1 +=1
multi_table()


# 4) переробити# це# завдання# під# меню
#
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
while True:
    print('1. знайти мін. число')
    print('2. видалити усі дублікати')
    print('3. замінити кожне 4 - те значення на ‘X’ ')
    print('4. вивести на екран пустий квадрат з “ * ”, сторона якого вказана як аргумент функції')
    print('5. вивести табличку множення за допомогою циклу while ')
    print('6. вихід')

    choice = input('Зробіть свій вибір: ')
    if choice == '1':
        print(min(list))
    elif choice == '2':
        print(set(list))
    elif choice == '3':
        to_x()
    elif choice == '4':
        quadra_def(5)
    elif choice == '5':
        multi_table()
    elif choice == '6':
        break