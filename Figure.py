class Figure:
    pass


class Point(Figure):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r


class Polygon(Figure):
    def __init__(self, *points):
        self.points = points


class Line(Polygon):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)


class Triangle(Polygon):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)


class IsoscelesTriangle(Triangle):
    def __init__(self, p1, p2, l):
        p2.x = p2.x - p1.x
        p2.y = p2.y - p1.y
        p1.x = 0
        p1.y = 0
        c = (-p2.x ** 2 - p2.y ** 2) / (-2)
        if p2.x != 0:
            a = p2.y ** 2 + p2.x ** 2
            b = -2 * p2.y * c
            e = c ** 2 - l ** 2 * p2.x ** 2
            d = b ** 2 - 4 * a * e
            m = (-b + d ** (1 / 2)) / (2 * a)
            n = (c - m * p2.y) / p2.x
        else:
            m = c / p2.y
            n = (l ** 2 - (c ** 2) / p2.y ** 2) ** (1 / 2)
        p3 = Point(n, m)
        super().__init__(p1, p2, p3)


class Rectangle(Polygon):
    def __init__(self, l_d, r_u):
        l_u = Point(l_d.x, r_u.y)
        r_d = Point(r_u.x, l_d.x)
        super().__init__(l_d, l_u, r_d, r_u)


class Square(Rectangle):
    def __init__(self, p, l):
        l_d = p
        r_u = Point(p.x + l, p.y + l)
        super().__init__(l_d, r_u)







