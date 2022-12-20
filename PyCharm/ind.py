#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sum_start - функция, принимающая начальную сумму(start)
# возвращает декоратор
def sum_start(start):
    # декоратор
    def decorator(func):
        # Функция - обёртка
        def wrapped(*args, **kwarg):
            # Получаем сумму чисел в листе из ф-и num_sum()
            n_s = func(*args, **kwarg)
            # Возвращаем сумму с начальным счетчиком
            return n_s + start

        return wrapped

    return decorator


# Вызывается функция sum_start(), возвращающая декоратор
@sum_start(5)
def num_sum(s):
    num_list = [int(x) for x in s.split()]
    return sum(num_list)


if __name__ == '__main__':
    st = input("Enter the numbers separated by a space: ")
    print(num_sum(st))
