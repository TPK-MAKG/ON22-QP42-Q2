import os

class Character:
  def __init__(self,Name,XCoord,YCoord):
    self.__Name = Name #Name is declared as string
    self.__XVal = XCoord #x-coordinate is declared as integer
    self.__YVal = YCoord #y-coordinate is declared as integer
  def getName(self):
    return self.__Name
  def getX(self):
    return self.__XVal
  def getY(self):
    return self.__YVal
  def ChangePosition(self,NewX,NewY):
    self.__XVal = NewX
    self.__YVal = NewY
    
Characters = [Character(" ",-1,-1) for i in range(10)]

GameFile = open('Characters.txt','r')
for i in range(10):
  CharName = GameFile.readline()
  CharX = GameFile.readline()
  CharY = GameFile.readline()
  Characters[i] = Character(CharName,CharX,CharY)
  #or Characters[i].Name = CharName
#could also use a method for initializatiion in class declaration

Found = False
while Found == False:
  SearchName = input("Please enter a name:")
  for i in range(10):
    if Characters[i].CharName == SearchName:
      Found = True
      Index = i
      
while Moved == False:
  Direction = input("Which direction to move?")
  if Direction == 'A':
    XValue = Characters[Index].getX()
    YValue = Characters[Index].getY()
    Characters[Index].ChangePosition(XValue - 1, YValue)
    Moved = True
    print(Characters[Index], " has changed co-ordinates to x = ", XValue - 1," and y = ", YValue) 
  elif Direction == 'S':
    XValue = Characters[Index].getX()
    YValue = Characters[Index].getY()
    Characters[Index].ChangePosition(XValue, YValue - 1)
    Moved = True
    print(Characters[Index], " has changed co-ordinates to x = ", XValue," and y = ", YValue - 1) 
  elif Direction == 'W':
    XValue = Characters[Index].getX()
    YValue = Characters[Index].getY()
    Characters[Index].ChangePosition(XValue, YValue + 1)
    Moved = True
    print(Characters[Index], " has changed co-ordinates to x = ", XValue," and y = ", YValue + 1) 
  elif Direction == 'D':
    XValue = Characters[Index].getX()
    YValue = Characters[Index].getY()
    Characters[Index].ChangePosition(XValue + 1, YValue) 
    Moved = True
    print(Characters[Index], " has changed co-ordinates to x = ", XValue + 1," and y = ", YValue)     



Amal = Character("Amal",2,5)
print(Amal.getName())
print(Amal.getX())
print(Amal.getY())
Amal.ChangePosition(6,1)
print(Amal.getName())
print(Amal.getX())
print(Amal.getY())

