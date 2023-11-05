class Dog:
    def walk(self):
        print("*walking*")
    
    def speak(self):
        return "Woof!"
    
    
class Terrier(Dog):
    def speak(self):
        return "Arff!"
    

bobo = Terrier()    
bobo.walk()