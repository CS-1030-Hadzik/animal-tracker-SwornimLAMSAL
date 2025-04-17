from animal import Animal

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    
    def speak(self):
        # Must PRINT (not return) the message
        print("The dog barks.")
    
    def __str__(self):
        # Note the space after "Breed:" - this is crucial!
        return f"{super().__str__()}, Breed: {self.breed}"