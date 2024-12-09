import math
from re import match


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if self.__is_valid_color(*color):
            self.__color = list(color)
        else:
            self.__color = [0,0,0]
        if self.__is_valid_side(*sides) and len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.filled = False

    def get_color (self):
        return self.__color

    def set_color (self, r, g, b):
        if self.__is_valid_color (r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color (self, r, g, b):
        return all (isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def __is_valid_side (self, *sides):
        return  all (isinstance (side, int)  and side > 0 for side in sides)

    def get_sides (self):
        return self.__sides

    def set_sides (self, *new_sides):
        if self.__is_valid_side(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color,*sides):
        super().__init__(color, )
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square (self):
        return math.pi * self.__radius ** 2

    def __len__(self):
        return int(2 * math.pi * self.__radius)


class Triangle:
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side_length = sides[0] if len(sides) == 1 else 1
        super().__init__(color, *(side_length,) * 12)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())  

# Создаём куб с рёбрами длиной 3
cube2 = Cube((100, 150, 200), 3)
print(cube2.get_volume())

# Изменяем стороны
cube2.set_sides(4)
print(cube2.get_volume())


