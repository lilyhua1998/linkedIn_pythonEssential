# Python code​​​​​​‌​‌‌​‌‌​‌‌​​​​‌‌‌​​​‌​‌​​ below
class Shape:
  printChar = '#'

  def __init__(self):
    self.width=5
    self.height=5

  def printRow(self, i):
    raise NotImplementedError("Will be implemented by children extending this class")

  def print(self):
    for i in range(self.height):
      self.printRow(i)


class Square(Shape):
  def printRow(self, i):
    print(self.printChar * self.width)




class Triangle(Shape):
  #right-angle
  #def printRow(self, i):
    #print(self.printChar * (i+1))

  def printRow(self, i):
    #align height only
    perTriWidth=i*2+1
    triWidth=self.height*2 #around 2:1 (width:height
    
    blank= int((triWidth-perTriWidth)/2)
    print(" " * blank  + self.printChar * perTriWidth )
    



triangle=Triangle()
triangle.print()
