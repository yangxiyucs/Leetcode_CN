class Student:
    def __init__(self, name, age, sex):
       self.name = name
       self.age = name
       self.sex = name
    def study(self):
        print(f'我叫{self.name},今年{self.age}岁，性别{self.sex}, 我要去学习啦')

    def rest(self):
        print(f'我叫{self.name},今年{self.age}岁，性别{self.sex}, 我要去休息啦')

a1 = Student('李诗',18,'女')
a2 = Student('张山',18,'男')
a1.study()
a2.rest()
