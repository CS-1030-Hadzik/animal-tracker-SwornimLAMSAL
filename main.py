from animal import Animal
from dog import Dog

def main():
    # Test Animal class
    generic_animal = Animal("Generic", "Unknown")
    print(generic_animal)  # Tests __str__
    generic_animal.speak()  # Tests speak method

    # Test Dog class
    buddy = Dog("Buddy", "Canine", "Golden Retriever")
    print(buddy)  # Tests overridden __str__
    buddy.speak()  # Tests overridden speak method

    # Test class-level list
    print("\nAll Animals:")
    for animal in Animal.all_animals:
        print(animal)

if __name__ == "__main__":
    main()