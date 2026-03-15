class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = False
   
   
    def describe(self):
        status = "Adopted" if self.adopted else "Waiting for new home"
        print(f"{self.name}, {self.species}, {self.age} years old - {status}")

    def adopt_animal(self):
        if not self.adopted:
            self.adopted = True 
            print(f"{self.name} found a forever home!!")
        else:
            print(f"{self.name} was already adopted")  

cat = Animal("Panda", "Cat", 14)
cat.adopt_animal()
cat.describe()