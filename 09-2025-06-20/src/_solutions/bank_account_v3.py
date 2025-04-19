class BankAccount:
    def __init__(self, bank_name, customer_name, pin):
        self.bank_name = bank_name
        self.customer_name =  customer_name
        self.__pin = pin
        self.__balance = 0
        self.__locked = False
        self.__failed_attempts = 0
    
    def __str__(self):
        return f'This {self.bank_name} account belongs to {self.customer_name}'

    def print_bank_name(self):
        print('My name is', self.bank_name)
         
    def print_customer_name(self):
        print('This account belongs to', self.customer_name)
                
    def get_balance(self):
        return self.__balance
    
    def check_pin(self):
        if not self.__locked:
            input_pin = input('Please enter your PIN: ')
            if input_pin == self.__pin:
                self.__failed_attempts = 0
                return True
            else:
                print('Wrong PIN')
                self.__failed_attempts += 1
                if self.__failed_attempts == 3:
                    self.__locked = True
        else:
            print('Your account is locked.')
        
        return False
        
    def deposit(self, amount):
        if self.check_pin():
            self.__balance += amount
            print('Your amount got deposited.')

    def withdraw(self, amount):
        if self.check_pin():
            if self.__balance - amount < 0:
                print(f'Insufficient funds.')
            else:
                self.__balance -= amount