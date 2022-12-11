from dateutil.utils import today


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def print_info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}')

    @classmethod
    def generate_person(cls, name, year):
        age = today().year - year
        return cls(name, age)

    @staticmethod
    def check_adult(person):
        if person.age >= 18:
            return True
        else:
            return False


def main():
    person1 = Person('Lisa', 20)
    person1.print_info()

    misha = Person.generate_person('Misha', 2020)
    print(misha)

    print(Person.check_adult(misha))
    print(Person.check_adult(person1))


main()

