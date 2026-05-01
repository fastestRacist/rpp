class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(x, y, z):
    if  x <= 0 or y <= 0 or z <= 0 or x + y <= z or x + z <= y or y + z <= x:
        raise IncorrectTriangleSides
    elif x == y == z:
        return "equilateral"
    elif x == y or y == z or x == z:
        return "isosceles"
    else:
        return "nonequilateral"
