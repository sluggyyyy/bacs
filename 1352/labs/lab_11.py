import random
class Pet:
    def __init__(self, n: str = 'Unknown name', a: float = 0):
        self.name = n
        self.age = a
    
    def __str__(self):
        return f'Pet Information:\n\tName: { self.name }\n\tAge: { self.age }'
    
    def make_noise(self):
        print(f"{self.name} makes a generic pet noise")
        
    def make_noise_twice(self):
        Pet.make_noise(self)
        Pet.make_noise(self)

# TODO: create a class called Cat that is derived from the base class Pet
    # TODO: the __init__ method has three parameters, 
    # representing name (str), age (float) and color (str).
    # The default values should be self.name = "Unknown name" 
    # and self.age = 0 and self.color = 'Unknown color'
    # Call the __init__ method for Pet, using the name and age as the arguments.
    # Then set the instance variable color using the third passed argument. 
class Cat(Pet):
    def __init__(self, n = 'Unknown name', a = 0, c = 'Unknown color'):
        super().__init__(n, a)
        self.color = c

    # TODO: the __str__ method should call the __str__ method for Pet, then combine that result
    # with the information stored in color to produce the return value according to the sample
    # output given in the instructions
    def __str__(self):
        return f'{super().__str__()}\n\tCat color: {self.color}'
    
    def make_noise(self):
        print(f'{self.name} says Meow!')

# TODO: create a class called Dog that is derived from the base class Pet
    # TODO: the __init__ method has three parameters, 
    # representing name (str), age (float) and breed (str)
    # The default values should be: self.name =“Unknown name”, 
    # self.age = 0, and, self.breed = ‘Unknown breed’
    # Call the __init__ method for Pet, using the name and age as the arguments.
    # Then set the instance variable breed using the third passed argument
class Dog(Pet):
    def __init__(self, n = 'Unknown name', a = 0, b = 'Unknown breed'):
        super().__init__(n, a)
        self.breed = b
    # TODO: the __str__ method should call the __str__ method for Pet, then combine that result
    # with the information stored in breed to produce the return value according to the sample
    # output given in the instructions
    def __str__(self):
        return f'{super().__str__()}\n\tDog breed: {self.breed}'
    
    def make_noise(self):
        print(f'{self.name} says Woof!')

# test code:
def test_pet_lab_part1():
    # all of the following four instantiations should work
    c1 = Cat()
    c2 = Cat("c2")
    c3 = Cat("c3", 10)
    c4 = Cat("c4", 10, "Calico")
    # Confirm types
    assert issubclass(Cat, Pet), "Cat should be a subclass of Pet, and it isn't"
    assert isinstance(c1, Pet), "Every Cat should also be a Pet object, and it is not"
    # Confirm values properly assigned
    assert c1.name == "Unknown name", "Default name for Cat not initialized correctly"
    assert c1.age == 0, "Default age for Cat not initialized correctly"
    assert c1.color == "Unknown color", "Default color for Cat not initialized correctly"
    assert c4.name == "c4", "Cat name not initialized correctly"
    assert c4.age == 10, "Cat age not initialized correctly"
    assert c4.color == "Calico", "Cat color not initialized correctly"
    # Confirm correct output
    assert c1.__str__() == "Pet Information:\n\tName: Unknown name\n\tAge: 0\n\tCat color: Unknown color", "Output for Cat information is not correct"
    assert c4.__str__() == "Pet Information:\n\tName: c4\n\tAge: 10\n\tCat color: Calico", "Output for Cat information is not correct"
    # all of the following four instantiations should work
    d1 = Dog()
    d2 = Dog("d2")
    d3 = Dog("d3", 10)
    d4 = Dog("d4", 10, "Mixed")
    # Confirm types
    assert issubclass(Dog, Pet), "Dog should be a subclass of Pet, and it isn't"
    assert isinstance(d1, Dog), "Every Dog should also be a Pet object, and it is not"
    # Confirm values properly assigned
    assert d1.name == "Unknown name", "Default name for Dog not initialized correctly"
    assert d1.age == 0, "Default age for Dog not initialized correctly"
    assert d1.breed == "Unknown breed", "Default breed for Dog not initialized correctly"
    assert d4.name == "d4", "Dog name not initialized correctly"
    assert d4.age == 10, "Dog age not initialized correctly"
    assert d4.breed == "Mixed", "Dog breed not initialized correctly"
    # Confirm correct output
    assert d1.__str__() == "Pet Information:\n\tName: Unknown name\n\tAge: 0\n\tDog breed: Unknown breed", "Output for Dog information is not correct, d1"
    assert d4.__str__() == "Pet Information:\n\tName: d4\n\tAge: 10\n\tDog breed: Mixed", "Output for Dog information is not correct, d4"
    print("All tests passed.")

def main(): 
    # TODO: instantiate a Cat object with name 'Bill', age 22 and color 'Orange', save in a variable called bill
    # TODO: instantiate a Dog object with name "Snoopy', age 72, and breed "Beagle', save in a variable called snoopy
    
    # Seed the random number generator with the output. The output
    # has to match the required output to get the same random number
    
    pet_list = [Cat('Bill', 22, 'Orange'), Dog('Snoopy', 72, 'Beagle'), Pet('Sandy', 13), Cat('Meowth', 8, 'Yellow'), Dog('Scooby Doo', 6, 'Great Dane')]
    
    for pet in range(len(pet_list)):
        if pet_list[pet] == pet_list[0] or pet_list[pet] == pet_list[-1]:
            pet_list[pet].make_noise_twice()
        else:
            pet_list[pet].make_noise()

    # FYI, the output should be:
    # Pet Information:
    # 	Name: Bill
    # 	Age: 22
    # 	Cat color: Orange
    # Pet Information:
    # 	Name: Snoopy
    # 	Age: 72
    # 	Dog breed: Beagle

if __name__ == "__main__":
    main()
