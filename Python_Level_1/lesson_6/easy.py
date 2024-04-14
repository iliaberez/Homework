# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle():
    def __init__(self, pointA, pointB, pointC):
        self.pointA = Point(pointA[0], pointA[1])
        self.pointB = Point(pointB[0], pointB[1])
        self.pointC = Point(pointC[0], pointC[1])
    def calc_square(self):
        s = math.fabs((self.pointB.x - self.pointA.x)*(self.pointC.y - self.pointA.y)-(self.pointC.x - self.pointA.x)*(self.pointB.y-self.pointA.y))/2
        return s

    def calc_height(self):
        h = 2 * self.calc_square() / (math.sqrt((self.pointC.x - self.pointA.x)**2+(self.pointC.y - self.pointA.y)**2))
        print('H={:.2f}'.format(h))

    def calc_perimeter(self):
        p = math.sqrt((self.pointA.x - self.pointA.y)**2 +(self.pointB.x - self.pointB.y)**2 + (self.pointC.x - self.pointC.y)**2)
        print('P={:.2f}'.format(p))

triange = Triangle([-1,-3], [3,4], [5,-5])

print('S={:.2f}'.format(triange.calc_square()))
triange.calc_perimeter()
triange.calc_height()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid():
    def __init__(self, pointA, pointB, pointC, pointD):
        self.pointA = Point(pointA[0], pointA[1])
        self.pointB = Point(pointB[0], pointB[1])
        self.pointC = Point(pointC[0], pointC[1])
        self.pointD = Point(pointD[0], pointD[1])
        self._AB = math.sqrt((self.pointB.x - self.pointA.x)**2+(self.pointB.y - self.pointA.y)**2)
        self._BC = math.sqrt((self.pointC.x - self.pointB.x)**2+(self.pointC.y - self.pointB.y)**2)
        self._CD = math.sqrt((self.pointD.x - self.pointC.x)**2+(self.pointD.y - self.pointC.y)**2)
        self._AD = math.sqrt((self.pointD.x - self.pointA.x)**2+(self.pointD.y - self.pointA.y)**2)

    def check_trapezoid(self):
        if self._AB == self._CD:
            print('Равнобедренная трапеция')
        else:
            print('Не равнобедренная трапеция')

    def length_side(self):
        print('\nAB=',  self._AB)
        print('BC=',  self._BC)
        print('CD=',  self._CD)
        print('AD=',  self._AD)

    def calc_square(self):
        s = 0.5*(self._AD + self._BC)*math.sqrt(self._AB**2-((self._AD - self._BC)/2)**2)
        print('S={:.2f}'.format(s))
        return s

    def calc_perimeter(self):
        p = self._AB + self._BC + self._CD + self._AD
        print('P={:.2f}'.format(p))

trapezoid = Trapezoid([2,4],[0,2],[0,7],[2,5])
trapezoid.check_trapezoid()
trapezoid.length_side()
trapezoid.calc_perimeter()
trapezoid.calc_square()