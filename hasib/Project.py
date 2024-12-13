class Hasib():
    h = ''
    age = 0

a = Hasib()
a.h = "Hasib Sheikh"
a.age = 25
print(f"Name: {a.h}, Age: {a.age}")
print(a)


class Human():
    def __init__(self, h, age):
        self.h = h 
        self.age = age
        
    def humName(self):
        self.panjabi = True
        self.tupi = True 
        print("Hasib is a parfact boy") 
    
    
hasib = Human("Human HS", 10)
print(f"Name: {hasib.h}, Age: {hasib.age}")
hasib.humName()


