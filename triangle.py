# Небольшая задачка на ООП. Если все сделано, то можно за нее взяться. На звонке в пятницу на ее примере поговорм про ООП.
# Надо написать классы для треугольника и прямоугольника.
# - Для создания треугольника передаются три стороны,
# для прямоугольника две стороны.
# Также еще передается цвет фигуры.
# - У этих классов должен быть метод который выводит информацию о фигуре,
# что это за фигура и какие у нее параметры и цвет.
# И еще надо реализовать метод покраски - который принимает на вход цвет
# и меняет цвет фигуры на новый.
# Если цвет такой же, то выводится сообщение, что фигура уже такого же цвета.
# - Также у этих классов должны быть методы расчета периметра и площади.
class Figure:
    def __init__(self, sides,color):
        if type(sides) != dict:
            raise ValueError("Стороны задаются в виде {'a':5,'b':6}")
        self.sides = sides
        self.color = color

    def __repr__(self):
        return f"Figure, color: {self.color} sides: {str(self.sides)}"

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        perimeter = 0
        for side in self.sides.keys():
            perimeter += self.sides[side]
        return perimeter

    def change_color(self,new_color):
        if new_color==self.color:
            print(f"Фигура уже такого цвета. Цвет: {self.color}")
        else:
            self.color = new_color


class Rectangle(Figure):
    def __init__(self, sides, color):
        if len(sides) != 2:
            raise ValueError("У прямоугольника нужно передавать 2 стороны")
        super().__init__(sides, color)

    def __repr__(self):
        return f"Rectangle, color: {self.color}, sides: {str(self.sides)}"

    def area(self):
        area = 1
        for side in self.sides.keys():
            area *= self.sides[side]
        return area


class Triangle(Figure):
    def __init__(self, sides, color):
        if len(sides) != 3:
            raise ValueError("У треугольника нужно передавать 2 стороны")
        else:
            super().__init__(sides, color)

    def __repr__(self):
        return f"Triangle, color: {self.color}, sides: {str(self.sides)}"

    def area(self):
        p = self.perimeter()/2
        area = 1
        for side in self.sides.keys():
            area *= p-self.sides[side]

        area = (p*area)**0.5

        return area

