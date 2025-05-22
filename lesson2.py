# 1) написати функцію(notebook)# на# замикання, котра# буде
# в# собі# зберігати# список# справ, вам потрібно реалізувати# два# методи: – перший
# записує# в# список# нову# справу# – другий# повертає# всі# запис# (прикла# сигнатури
# функції# notebook# у# вкладенні )
#
# 1111111111111111111111111111111111111111111111111111111111111111111111111111111
from itertools import count


def notebook():
    todo_list = ['work', 'study', 'eat', 'sleep']

    def add_todo(todo):
        nonlocal todo_list
        return todo_list + todo


    def get_all():
        nonlocal todo_list
        print(todo_list)
        return todo_list


    return add_todo, get_all


add_1, get_all1 = notebook()
add_2, get_all2 = notebook()
print(add_1(['cook']))
print(add_2(['homework']))
print(add_1(['wash']))
print(add_2(['wash']))

# ************************************************************

def notebook():
    todo_list = ['work', 'study', 'eat', 'sleep']

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)


    def get_all():
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


notebook_1, get_1 = notebook()
notebook_2, get_2 = notebook()
notebook_1('cook')
notebook_2('homework')
notebook_1('wash')
notebook_2('wash')

print(get_1())
print(get_2())


# 2222222222222222222222222222222222222222222222222222222222222222222222
# 2) протипізувати# перше# завдання

from typing import Callable

def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = ['work', 'study', 'eat', 'sleep']

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)


    def get_all():
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


notebook_1, get_1 = notebook()
notebook_2, get_2 = notebook()
notebook_1('cook')
notebook_2('homework')
notebook_1('wash')
notebook_2('wash')

print(get_1())
print(get_2())




# 3) створити# функцію, котра# буде# повертати# суму
# розрядів# числа# у# вигляді# строки(також# використовуємо# типізацію)
#
# Приклад:
# # expanded_form(12)  # return ’10 + 2′
# # expanded_form(42)  # return ’40 + 2′#
# expanded_form(70304)  # return ‘70000 + 300 + 4’

def expanded_form (num):
    st = str(num)
    length = len(st) - 1
    res = []
    for i, ch in enumerate(st):
        if ch != '0':
            res.append(ch + '0' * (length - i))
    print(' + '.join(res))
    return ' + '.join(res)


expanded_form('758')



# 4) створити# декоратор, котрий# буде# підраховувати, скільки# разів# була
# запущена# функція, продекорована# цим# декоратором, та# буде# виводити# це# значення
# після# виконання# функцій#
# приклад# декоратору# у# вкладенні

def decor (func):
    counter = 0

    def inner (*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f'count: {counter}')
        func(*args, **kwargs)
        print('-'* 20)


    return inner


@decor
def func1():
    print('func1')

@decor
def func2():
    print('func2')

func1()
func1()
func2()
func1()