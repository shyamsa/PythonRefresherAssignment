'''
Created on Jul 18, 2020

@author: Shyam Sundar Ashok
'''

class Bank:
    def __init__(self,IFSC_Code,bankname,branchname,loc):        
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc

class Customer:
    def __init__(self,CustomerID,custname,address,contactdetails):
        self.CustomerID = CustomerID
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails

class Account(Bank):
    def __init__(self):
        Bank.__init__(self, "91874885", "Bank of America", "Manhattan","New York")
        self.balance = 5000
           
    customer = Customer("1234", "Warren Buffett", "651 S 55th Street Omaha NE", "Warren.Buffett@berkshirehathaway.com")
    
    def getAccountInfo(self):
        print("\n Welcome: ", self.customer.custname, " to your",self.bankname," account") 
        
    def deposit(self, amount):
            self.balance += amount 
            print("\n Sucessfully Deposited:", amount) 
        
    def widthraw(self, amount):
            self.balance -= amount
            print("\n Sucessfully Withdrawn:", amount)  
    
    def getBalance(self):
            print("\n Your Balance is :", self.balance)

class SavingsAccount(Account):
    def __init__(self, minimum_balance):
        Account.__init__(self)
        self.minimum_balance = minimum_balance
        
    def getAccountInfo(self):
        Account.getAccountInfo(self)
        
    def deposit(self):
        amount = float(input("Enter amount to be deposited: ")) 
        Account.deposit(self, amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: ")) 
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            Account.widthraw(self, amount)
            
    def getBalance(self):
        Account.getBalance(self)

# creating an object of class 
s = SavingsAccount(1000) 
   
# Calling functions with that class object 
s.getAccountInfo()
s.deposit() 
s.withdraw() 
s.getBalance()

    