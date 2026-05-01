class IncorrectTriangleSides(Exception):
    pass


class Triangle:

    def __init__(self, x, y, z):
        if x <= 0 or y <= 0 or z <= 0 or x + y <= z or x + z <= y or y + z <= x:
            raise IncorrectTriangleSides

        self.x = x
        self.y = y
        self.z = z

    def triangle_type(self):
        if self.x == self.y == self.z:
            return "equilateral"
        elif self.x == self.y or self.y == self.z or self.x == self.z:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.x + self.y + self.z