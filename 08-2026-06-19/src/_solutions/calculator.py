class calculator:
    def __init__(self):
        
        self.save = 0
        self.result = 0
    
    def __str__(self):
        return f'This is a simple calculator'

    def add_numbers(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        
        print(f'The sum of {self.var1} and {self.var2} is {self.var1 + self.var2}')
        
    def save_result(self):
        self.save = self.var1 + self.var2
        print('Result saved!')