import unittest
from unittest.mock import patch
from io import StringIO
from animal import Animal
from dog import Dog

class TestAnimals(unittest.TestCase):
    total_points = 0  # Class-level variable to track points
    user_name = ""  # Class-level variable to store the user's name

    @classmethod
    def setUpClass(cls):
        # Ask for the user's name before tests start
        cls.user_name = input("What is your name?")

    def test_animal_initialization(self):
        generic_animal = Animal("Generic", "Unknown")
        self.assertEqual(generic_animal.name, "Generic")
        self.assertEqual(generic_animal.species, "Unknown")
        self.assertEqual(Animal.kingdom, "Animalia")
        TestAnimals.total_points += 10
        print(".test_animal_initialization passed: +10 points")

    @patch('sys.stdout', new_callable=StringIO)
    def test_animal_speak(self, mock_stdout):
        generic_animal = Animal("Generic", "Unknown")
        generic_animal.speak()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "The animal makes a noise.")
        TestAnimals.total_points += 10
        print(".test_animal_speak passed: +10 points")

    def test_animal_str(self):
        generic_animal = Animal("Generic", "Unknown")
        self.assertEqual(str(generic_animal), "Kingdom: Animalia, Name: Generic, Species: Unknown")
        TestAnimals.total_points += 10
        print(".test_animal_str passed: +10 points")

    def test_dog_initialization(self):
        buddy = Dog("Buddy", "Canine", "Golden Retriever")
        self.assertEqual(buddy.name, "Buddy")
        self.assertEqual(buddy.species, "Canine")
        self.assertEqual(buddy.breed, "Golden Retriever")
        TestAnimals.total_points += 10
        print(".test_dog_initialization passed: +10 points")

    @patch('sys.stdout', new_callable=StringIO)
    def test_dog_speak(self, mock_stdout):
        buddy = Dog("Buddy", "Canine", "Golden Retriever")
        buddy.speak()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "The dog barks.")
        TestAnimals.total_points += 10
        print(".test_dog_speak passed: +10 points")

    def test_dog_str(self):
        buddy = Dog("Buddy", "Canine", "Golden Retriever")
        self.assertEqual(str(buddy), "Kingdom: Animalia, Name: Buddy, Species: Canine, Breed: Golden Retriever")
        TestAnimals.total_points += 10
        print(".test_dog_str passed: +10 points")

    def test_all_animals(self):
        Animal.all_animals = []  # Reset list for testing
        generic_animal = Animal("Generic", "Unknown")
        buddy = Dog("Buddy", "Canine", "Golden Retriever")
        self.assertIn(generic_animal, Animal.all_animals)
        self.assertIn(buddy, Animal.all_animals)
        self.assertEqual(len(Animal.all_animals), 2)
        TestAnimals.total_points += 10
        print("test_all_animals passed: +10 points")

    @classmethod
    def tearDownClass(cls):
        # Print the total points and the user's name
        print(f"\nTotal Points: {cls.total_points}/70")
        print(f"Great job, {cls.user_name}!")
        if cls.total_points == 70:
            print("Congratulations! You passed all tests.")
        print("\n---")
        print(f"Ran 7 tests in {0:.3f}s")  # Time will be filled by unittest

if __name__ == "__main__":
    unittest.main()