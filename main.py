from math import sqrt

"""
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216
"""


class Figure:
    sides_count = 0
    __sides = []
    __color = []

    def __init__(self, color, *sides, filled=False):
        if len(sides) != self.sides_count:
            self.__sides = '1' * self.sides_count
        else:
            self.__sides = [i for i in sides]
        self.__color = list(color)
        self.filled = filled

    def name_(self):
        """
        Возвращает имя Класса вызванного объекта
        """

        return f'{self.__class__.__name__}'


    def get_color(self):
        """
        Возвращает список RGB цветов
        """

        return f'Цвет {self.name_()}: {self.__color}'

    def __is_valid_color(self, r, g, b):
        """
        Служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
        перед установкой нового цвета
        """
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            print('Ошибка! Цвета должны быть в диапазоне от 0 до 255')
            return False

    def set_color(self, r, g, b):
        """
        Принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие
        значения, предварительно проверив их на корректность
        """

        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        """
        Служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
        положительные числа и кол-во новых сторон совпадает с текущим
        """

        return (len(sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in sides))

    def get_sides(self):
        """
        Возвращает значение атрибута __sides
        """

        return self.__sides

    def __len__(self):
        """
        Возвращает периметр фигуры
        """

        perimetr = int(sum(self.__sides))
        return perimetr

    def set_sides(self, *new_sides):
        """
        Принимает новые стороны, если их количество не равно sides_count, то не изменять, в
        противном случае - менять
        """

        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        """
        Возвращает радиус круга
        """

        return f'{len(self) * (2/3.14)}'

    def get_square(self):
        """
        Возвращает площадь круга
        """

        return f'{((len(self))**2)/(4*3.14)}'


class Triangle(Figure):
    """
    Все атрибуты и методы класса Figure
    Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
    Метод get_square возвращает площадь треугольника.
    """

    sides_count = 3
    __height = 0

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=False)
        a, b, c = [value for value in sides]
        if a < b + c and b < a + c and c < a + b:
            self.__sides = [a, b, c]

    def get_height(self):
        print(self.__len__)
        p = int(len(self))/2      #Полупериметр
        self.__height = (2/self.__sides[0])*sqrt((p*(p-self.__sides[0])*(p-self.__sides[1])*(p-self.__sides[2])))
        return f'{self.__height}'


    def get_square(self):
        pass


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=False)
        if len(sides) == 1:
            self.__sides = list(sides) * self.sides_count
        else:
            self.__sides = '1' * self.sides_count

    def get_sides(self):
        """
        Возвращает значение атрибута __sides
        """

        return self.__sides

    def get_volume(self):
        """
        Возвращает объем куба
        """

        return f'Объем {self.name_()}: {int(self.__sides[0]) ** 3}'


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    triangle1 = Triangle((10, 10, 10), 3, 4, 5)
    #triangle2 = Triangle((10, 10, 10), 3)

    # Проверка на изменение цветов:
    print('Проверка на изменение цветов:')
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    print('Проверка на изменение сторон:')
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print('Проверка периметра (круга), это и есть длина:')
    print(len(circle1))

    # Проверка объёма (куба):
    print('Проверка объёма (куба):')
    print(cube1.get_volume())

    print('Площадь круга')
    print(circle1.get_square())
    print('Высота треугольника')
    print(triangle1.get_height())


