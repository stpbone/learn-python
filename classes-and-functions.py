class Person:
  def __init__(self, name, age, height, weight, ftp):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
    self.ftp = ftp


  def myfunc(self):
    print("Hello my name is " + self.name)

  def myftp(self):
    print("My ftp is " + self.ftp)
    

p1 = Person("Simon Bone", "35 years old", "175cm tall", "69kg", "250 watts")
p1.myfunc()
p1.myftp()





