def get_trixngle_tzpe(x, y, z):
    if x + y <= z or x + z <= y or y + z <= x:
        return "Не существует"
    if x == y == z:
        return "equilateral"
    elif x == y or y == z or x == z:
        return "isosceles"
    else:
        return "nonequilateral"
