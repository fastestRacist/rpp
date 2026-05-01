import pytest
from triangle_class import Triangle, IncorrectTriangleSides


def test_create_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.x == 3
    assert triangle.y == 4
    assert triangle.z == 5


def test_equilateral():
    triangle = Triangle(3, 3, 3)
    assert triangle.triangle_type() == "equilateral"


def test_isosceles():
    triangle = Triangle(5, 5, 3)
    assert triangle.triangle_type() == "isosceles"


def test_nonequilateral():
    triangle = Triangle(4, 5, 6)
    assert triangle.triangle_type() == "nonequilateral"


def test_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter() == 12


def test_zero():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 5, 5)


def test_negative():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 5, 5)


def test_invalid():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)