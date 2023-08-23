# CHALLENGE 1
class point:
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqsum(self):
        return self.x**2 + self.y**2 + self.z**2

num= point(2,3,4)
print(num.sqsum())


# CHALLENGE 2


class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 / self.num1
cal= calculator(10,20)
print(cal.add())
print(cal.subtract())
print(cal.multiply())
print(cal.divide())

# CHALLENGE 3

class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, roll_number):
        self.__roll_number = roll_number

    def getRollNumber(self):
        return self.__roll_number


student = Student()


student.setName("shivam kumar")
student.setRollNumber(89)


name = student.getName()
roll_number = student.getRollNumber()


print("Name:", name) 
print("Roll Number:", roll_number)

# CHALLENGE 4

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate


account = Account("Ashish", 5000)


savings_account = SavingsAccount("Ashish", 5000, 5)


print("Account Title:", account.title)
print("Account Balance:", account.balance)


print("Savings Account Title:", savings_account.title)
print("Savings Account Balance:", savings_account.balance)
print("Savings Account Interest Rate:", savings_account.interestRate)

# CHALLENGE 5 
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.interestRate * self.balance) / 100


demo1 = SavingsAccount("Ashish", 2000, 5)


demo1.deposit(588)
balance_after_deposit = demo1.getBalance()
print("Balance after deposit:", balance_after_deposit)  

demo1.withdrawal(500)
balance_after_withdrawal = demo1.getBalance()
print("Balance after withdrawal:", balance_after_withdrawal)  

interest_amount = demo1.interestAmount()
print("Interest amount:", interest_amount)  


