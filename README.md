[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19221172&assignment_repo_type=AssignmentRepo)
# Assignment: Testing the Animal and Dog Classes

## Objective
The purpose of `main.py` is to create and test the `Animal` and `Dog` classes to demonstrate object-oriented programming concepts, including class-level attributes, instance methods, inheritance, and method overriding.

## Tasks for `main.py`

1. **Import Classes**:
   - Import the `Animal` class from `animal.py`.
   - Import the `Dog` class from `dog.py`.

2. **Create and Test an Animal Instance**:
   - Create an instance of the `Animal` class with a name and species.
   - Print the instance to verify the `__str__` method.
   - Call the `speak` method to ensure it outputs the correct message.

3. **Create and Test a Dog Instance**:
   - Create an instance of the `Dog` class with a name, species, and breed.
   - Print the instance to verify the overridden `__str__` method.
   - Call the `speak` method to ensure it outputs the correct message for a dog.

4. **Test the Class-Level List**:
   - Access the `all_animals` list in the `Animal` class.
   - Print the list to verify that it contains all instances of `Animal` and `Dog`.


# Task: Implement the Animal Class

## Objectives
1. **Class-Level Attribute**:
   - Create a class-level attribute (e.g., `all_animals`) that stores all instances of the `Animal` class.

2. **Constructor (`__init__`)**:
   - The `__init__` method should accept:
     - `name`: Name of the animal.
     - `species`: The species of the animal.
   - Add each new `Animal` instance to the class-level `all_animals` list.

3. **Add a `speak` Method**:
   - Add a method named `speak` that outputs a generic message.
   - Example: `"The animal makes a noise."`

4. **Implement the `__str__` Method**:
   - Return a formatted string with the following structure:
     ```
     Kingdom: {kingdom attribute}, Name: {name attribute}, Species: {species attribute}
     ```
# Task: Implement the Dog Class

## Objectives
1. **Constructor (`__init__`)**:
   - Write the `__init__` method for the `Dog` class.
   - The constructor should accept the following parameters:
     - `name`: The name of the dog.
     - `species`: The species of the dog (e.g., "Canine").
     - `breed`: The breed of the dog (e.g., "Golden Retriever").
   - Use `super().__init__()` to initialize the `name` and `species` attributes from the `Animal` class.
   - Set the `breed` attribute specific to the `Dog` class.

2. **Override the `__str__` Method**:
   - Override the `__str__` method to include the `breed` attribute in the string representation.
   - Example output:
     ```
     Kingdom: Animalia, Name: Buddy, Species: Canine, Breed: Golden Retriever
     ```

3. **Add a `speak` Method**:
   - Add a method named `speak` that outputs a specific message for dogs.
   - Example output: `"The dog barks."`

## Submission
- Implement the tasks in the `dog.py` file.
- Test your implementation in `main.py` by:
  - Creating a `Dog` instance.
  - Printing the `Dog` instance to verify the `__str__` method.
  - Calling the `speak` method.


## Example Output

Here’s the expected output when running the program:

The output includes:
1. The string representation of `Animal` and `Dog` objects.
2. The printed messages from their `speak` methods.
3. A listing of all objects stored in the `all_animals` list.



```plaintext
Kingdom: Animalia, Name: Generic, Species: Unknown
The animal makes a noise.
Kingdom: Animalia, Name: Buddy, Species: Canine, Breed: Golden Retriever
The dog barks.
All Animals:
Kingdom: Animalia, Name: Generic, Species: Unknown
Kingdom: Animalia, Name: Buddy, Species: Canine, Breed: Golden Retriever
```



## Submission
- Implement the tasks in the `animal.py` file.
- Upload a screenshot of your score by running TestAnimals.py

# Example
![Example Test Output](/images/test_run.png)
