class Pet:
    def __init__(self,name: str, specie: str, age:int):
        self.name = name
        self.specie = specie
        self.age = age
        self.happiness = 50
    
    def feed(self):
    ## Increases the pet's happiness by 10 and prints a message.
        self.happiness += 10
        print(f"{self.name} has been fed! Happiness level: {self.happiness}")
       

    def play(self):
     ## Increases the pet's happiness by 20 and prints a message.
     self.happiness += 20
     print(f"{self.name} is playing! Happiness level: {self.happiness}")
      
    
    def sleep(self):
    ## Increases the pet's happiness by 5 and prints a message.
        self.happiness += 5
        print(f"{self.name} is playing! Happiness level: {self.happiness}")


    def describe(self):
       print(f"{self.name} is a {self.specie} and is {self.age} years old. Happiness level: {self.happiness} ")