class BankAccount:
    def __init__(self, bank_name, customer_name):
        self.bank_name = bank_name
        self.customer_name = customer_name
    
    def print_bank_name(self):
        print(f"My name is {self.bank_name}")
        
    def print_customer_name(self):
        print(f"This account belongs to {self.customer_name}")