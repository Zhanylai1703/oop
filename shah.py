class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, num):
        self.num = num
        return f'через {self.num} года {self.name} исполнится {self.age + self.num} лет'

anne = Person('Anna', 16, 'male')
print(anne.calculate_age(3))


