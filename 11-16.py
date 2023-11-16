class Student:
    def __init__(self,name,age):
        self.name = name

        self.age = age

    def __str__(self):
        return f'Name : {self.name} Age : {self.age}'

    def myfunc(self):
        print('Name : {} Age: {}'.format(self.name,self.age))

p1 = Student('Ben',10)

p2 = Student('Alice' , 20)

p1.myfunc()

p2.myfunc()

class Teacher:
    pass