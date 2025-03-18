from abc import ABC, abstractmethod
class ParentClass:
    def __init__(self) -> int:
       pass

    def add(self, first_operand:int, second_operand:int) -> int:
            return first_operand + second_operand 
    @abstractmethod
    def add(self, first_operand:str, second_operand:str) -> str:
            return f'{first_operand} + {second_operand}'
    
    def sub(self, first_operand:int, second_operand:int) -> int:
        return first_operand - second_operand
    
    @abstractmethod
    def times(self,first_operand:int, second_operand:int):
         pass

class ChildClass(ParentClass): # inheritance
 def __init__(self) -> int:
     pass
 def times(self, first_operand:int, second_operand:int):
      return  first_operand * second_operand
     
pc = ParentClass()
print(pc.add(7,8))

child = ChildClass()
print(child.add(3,9))
print(pc.times(10,30))
print(child.times(10,30))

