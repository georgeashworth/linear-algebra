import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    def subtract(self, v):
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def scalar_multiply(self, c):
        return Vector([x * c for x in self.coordinates])

    def magnitude(self):
        return math.sqrt(sum([x * x for x in self.coordinates]))

    def direction(self):
        return self.scalar_multiply(1.0 / self.magnitude())
