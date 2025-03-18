class Math:
    def __init__(self,first_operand:int, second_operand:int, operand:str) -> int:
        self.first_operand = first_operand
        self.second_operand = second_operand
        self.operand = operand
    
    def __init__(self):
        pass

    def set_first_operand(self, first_operand:int):
       self.first_operand = first_operand
   
    def set_second_operand(self, second_operand:int):
       self.second_operand = second_operand
    
    def set_operand(self, operand:int):
       self.operand = operand
   
    def get_results(self):
        if self.operand == None:
            raise ValueError("Error: Invalid self.")
        
        if self.operand == 'add':
            return self.first_operand + self.second_operand
        elif self.operand == 'sub':
            return self.first_operand - self.second_operand
        else:
            raise ValueError("Error: Invalid operand")

