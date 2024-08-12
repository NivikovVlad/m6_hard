from math import sqrt, pi

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
        if isinstance(self, Triangle):
            if len(sides) == 1:
                self.__sides = list(sides) * self.sides_count
            elif len(sides) != self.sides_count:
                self.__sides = [1] * self.sides_count
            else:
                a, b, c = [value for value in sides]
                if a < b + c and b < a + c and c < a + b:
                    self.__sides = [a, b, c]
                else:
                    print('Такой треугольник создать невозможно, стороны будут = [1, 1, 1]')
                    self.__sides = [1] * self.sides_count

        elif isinstance(self, Cube):
            if len(sides) == 1:
                self.__sides = list(sides) * self.sides_count
            elif len(sides) != self.sides_count:
                self.__sides = [1] * self.sides_count
            else:
                self.__sides = sides

        elif isinstance(self, Circle):
            if len(sides) == 1:
                self.__sides = sides
            else:
                self.__sides = 1

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

        sides = self.get_sides()
        perimetr = sum(side for side in sides)
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
        return f'{round(((len(self))**2)/(4*3.14), 2)}'


class Triangle(Figure):
    """
    Все атрибуты и методы класса Figure
    Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
    Метод get_square возвращает площадь треугольника.
    """

    sides_count = 3
    __height = 0

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = self.get_sides()

    def get_height(self):
        p = int(len(self))/2      #Полупериметр
        self.__height = (2/self.sides[0])*sqrt((p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2])))
        return round(self.__height, 2)

    def get_square(self):
        square = 0.5 * self.sides[0] * self.get_height()
        return round(square, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self._sides = self.get_sides()

    def get_volume(self):
        """
        Возвращает объем куба
        """

        return f'Объем {self.name_()}: {self._sides[0] ** 3}'


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

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

    # Другие проверки
    print(f'\n\nДругие проверки')
    triangle1 = Triangle((10, 10, 10), 9, 4, 5)
    triangle2 = Triangle((10, 10, 10), 3)
    print('Cтороны треугольника1')
    print(triangle1.get_sides())
    print('Cтороны треугольника2')
    print(triangle2.get_sides())
    print('Площадь круга')
    print(circle1.get_square())
    print('Высота треугольника 1')
    print(triangle1.get_height())
    print('Высота треугольника 2')
    print(triangle2.get_height())
    print('Площадь треугольника1')
    print(triangle1.get_square())
    print('Площадь треугольника2')
    print(triangle2.get_square())
    ''''''

