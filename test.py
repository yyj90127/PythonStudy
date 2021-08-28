class Person():
    def __init__(self, name, gender):
        self.a = "调用父类的属性"
        print(name,gender)

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

if __name__ == '__main__':
    print(Student("SEVEN","male",77).a)