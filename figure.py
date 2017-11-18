"""
4. Создать абстрактный класс Figure с методами вычисления площади и периметра
, а также методом, выводящим информацию о фигуре на экран.
Создать производные классы: Rectangle (прямоугольник)
, Circle (круг)
, Triangle (треугольник) со своими методами вычисления площади и периметра.
Создать массив n фигур и вывести полную информацию о фигурах на экран.
"""

from abc import ABCMeta, abstractmethod


class figure:
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def show_info(self):
        pass

