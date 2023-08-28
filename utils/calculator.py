class Calculator:
    def __init__(self,num1,num2):
        self.numA = num1
        self.numB = num2
    
    def addition(self):
        return self.numA + self.numB
    
    def subtraction(self):
        return self.numA - self.numB
    
    def multiplication(self):
        return self.numA * self.numB
    
    def divide(self):
        if self.numB == 0:
            return "Dividing by zero is impossible"
        return self.numA / self.numB
    

