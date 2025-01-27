# class Student:
#     name = "test"
#     age = 20
#
#     def __int__(self, name, age):
#         print(f'{name} is {age} years old.')
#
# a = Student()


# class Student:
#     name = "test"
#     age = 20
#
#     def __int__(self):
#         print(f'{self.name} is {self.age} years old.')
#
# a = Student()


class student:
    def __int__(self, name, age):
        self.name = name
        self.age = age


    def printDetails(self):
        print(f'{self.name} is {self.age} years old')

s = student('Thisara',20)
s.printDetails()
