import math


class Figure:
    def dimention(self):
        raise NotImplementedError

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError


class TwoDimensionalFigure(Figure):
    def dimention(self):
        return "2D"

    def volume(self):
        return self.square()


class ThreeDimensionalFigure(Figure):
    def dimention(self):
        return "3D"

    def perimetr(self):
        raise Exception("3D figures do not have a perimeter")

    def square(self):
        raise Exception("3D figures do not have a single defined area")


class Circle(TwoDimensionalFigure):
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(TwoDimensionalFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def square(self):
        return self.width * self.height


class Triangle(TwoDimensionalFigure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimetr() / 2
        if s <= self.a or s <= self.b or s <= self.c:
            return 0  # Невалідний трикутник
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Ball(ThreeDimensionalFigure):
    def __init__(self, radius):
        self.radius = radius

    def squareSurface(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class RectangularParallelepiped(ThreeDimensionalFigure):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def squareSurface(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def squareBase(self):
        return self.length * self.width

    def height(self):
        return self.height

    def volume(self):
        return self.length * self.width * self.height


def parse_input(file_path):
    figures = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if parts:
                name = parts[0]
                parameters = list(map(float, parts[1:]))
                figures.append((name, parameters))
    return figures


def create_figure(name, params):
    if name == "Circle":
        return Circle(*params)
    elif name == "Rectangle":
        return Rectangle(*params)
    elif name == "Triangle":
        return Triangle(*params)
    elif name == "Ball":
        return Ball(*params)
    elif name == "RectangularParallelepiped":
        return RectangularParallelepiped(*params)
    else:
        return None


def find_largest_figure(file_paths):
    largest_figure = None
    max_measure = float('-inf')

    for file_path in file_paths:
        figures = parse_input(file_path)
        for name, params in figures:
            figure = create_figure(name, params)
            if figure:
                try:
                    measure = figure.volume()
                    if measure is not None and measure > max_measure:
                        max_measure = measure
                        largest_figure = (name, params, measure)
                except Exception:
                    continue

    return largest_figure


def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    largest_figure = find_largest_figure(input_files)

    with open("output.txt", "w") as file:
        if largest_figure:
            file.write(
                f"Largest Figure: {largest_figure[0]} with parameters {largest_figure[1]} and measure {largest_figure[2]:.2f}\n")
        else:
            file.write("No valid figures found.\n")
    print("Result saved to output.txt")


if __name__ == "__main__":
    main()
