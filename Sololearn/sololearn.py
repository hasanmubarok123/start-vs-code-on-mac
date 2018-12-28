# class Animal: 
#   def __init__(self, name, color):
#     self.name = name
#     self.color = color
    
#   def bark(self):
#     print("Woof!")

# class Cat(Animal):
#   def purr(self):
#     print("Purr...")
        
# class Dog(Animal):
#   def hoog(self):
#     print("Hoog!")

# fido = Dog("Fido", "brown")
# print(fido.name)
# print(fido.color)
# fido.bark()
# fido.hoog()

def countdown():
  i = 5
  while i > 0:
    yield i
    i -= 1

for i in countdown():
  print(i)