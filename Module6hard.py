class Figure:
    sides_count = 0

    def __init__(self, __color, __sides, filled=True):
        self.__color = __color
        self.__sides = __sides
        self.filled = filled

    def get_color(self):
        return [*self.__color]

    def __is_valid_color(self, r, g, b):
        valid_color = (r, g, b)
        for i in valid_color:
            if 0 <= i <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if not isinstance(i, int):
                    return False
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
        else:
            self.__sides = [self.__sides for i in range(self.sides_count)]


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides):
        self.sides_count = Circle.sides_count
        super().__init__(__color, __sides)
        self.__radius = __sides//6.28


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, __sides):
        self.sides_count = Triangle.sides_count
        super().__init__(__color, __sides)
        p = len(self) / 2
        sides = self.get_sides()
        self.side_a = sides[0]
        self.__height = (2 * (p * (p - sides[0]) * (p - sides[1]) *
                              (p - sides[2])) ** 0.5) / sides[0]

    def get_square(self):
        s = 0.5 * self.side_a * self.__height
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, __sides):
        self.sides_count = Cube.sides_count
        super().__init__(__color, __sides)

    def get_volume(self):
        cube_side = self.get_sides()[0]
        res = cube_side ** 3
        return res


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
print(cube1.get_volume())

