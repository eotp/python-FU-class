class Bank_Account: 
    from collections import namedtuple
    Interest = namedtuple('Interest', 'positive_balance negative_balance')

    def __init__(self, customer): 
        self.balance=0
        self.__interest = self.Interest(0.01, 0.12)
        self.customer = customer
        print(f"\nHi {self.customer}!!! Welcome, your account was created.") 
     
    def __str__(self):
        return f'\nThis is the bank account from {self.customer}.'
    
    def display(self): 
        print("\nNet Available Balance:", self.balance) 
        
    def deposit(self, amount): 
        self.balance += amount
        print(f"\nAmount Deposited: {amount}") 
  
    def withdraw(self, amount): 
        if self.balance>=amount: 
            self.balance-=amount 
            print(f"\nYou Withdrew: {amount}" ) 
        else: 
            print("\nInsufficient balance, you are in debt!") 
            self.balance-=amount 
          
    def interest(self):
        if self.balance == 0:
            print('Balance is at zero. No interest was charged.')
        else:
            if self.balance > 0:
                rate = self.__interest.positive_balance
                self.balance = self.balance + self.balance * rate
            
            elif self.balance < 0:
                rate = self.__interest.negative_balance
                self.balance = self.balance + self.balance * rate
            print(f'Interest at a rate of {int(rate*100)}% was charged.')

            
if __name__ == "__main__":
    s = Bank_Account('Mickey Mouse') 
    print(s)
    # Calling functions with that class object 
    s.deposit(1000) 
    s.withdraw(2000) 
    s.interest() 
    s.display() 