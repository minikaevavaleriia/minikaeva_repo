# фу вектора((((

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'x: {self.x}\n' \
               f'y: {self.y}\n' \
               f'z: {self.z}\n'

    def __add__(self, other):
        sum_vector = Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return sum_vector

    def __sub__(self, other):
        sub_vector = Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return sub_vector

    def __mul__(self, number):
        mul_vector = Vector3D(self.x * number, self.y * number, self.z * number)
        return mul_vector

def main():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(2, 1, 0)
    print(v1.__add__(v2))
    print(v1.__sub__(v2))
    print(v1.__mul__(4))
    print(v2.__mul__(-2))


main()
