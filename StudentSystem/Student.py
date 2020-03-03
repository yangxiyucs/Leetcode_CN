class Student():
  def __init__(self, name, gender, tel):
      self.gender = gender
      self.name = name
      self.tel = tel

  def __str__(self):
      return f'{self.gender}, {self.name}, {self.tel}'

stu1  = Student('erhuo', 'male', 12343123)
print(stu1)