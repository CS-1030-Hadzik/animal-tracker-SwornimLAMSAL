class Animal:
    all_animals = []
    kingdom = "Animalia"
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.all_animals.append(self)
    
    def speak(self):
        # Must PRINT (not return) the message
        print("The animal makes a noise.")
    
    def __str__(self):
        # Exact format required by tests
        return f"Kingdom: {self.kingdom}, Name: {self.name}, Species: {self.species}"
