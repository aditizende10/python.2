class bank:
    amount=50000

    print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    
    def deposit(self, d):
        if(d>0):
            self.amount+=balance
        else:
            print ("invalid")
    def withdraw(self, w):
        if (0<w<=self.amount):
            self.amount-=balance
        elif(w<=0):
            print ("invalid withdrawl amount:")
        else:
            print("Insufficient funds")
    def balance_check(self):
        print ("The amount is",self.amount)
obj=bank()
print ('1.' 'Deposit', '2.' ' Withdraw', '3.' 'Balance check')
for i in range (500) :
    choice=int (input ("Enter your choice:"))
    if (choice==1) :
        balance=int (input ("Enter the deposit amount: "))
        obj. deposit (balance)
        print ("Deposit is", balance)
    elif(choice==2):
        balance=int(input ("Enter the withdraw amount: "))
        obj.withdraw (balance)
        print("Withdraw is",balance)
    elif(choice==3):
        obj.balance_check()
    else:
        print("INVALID CHOICE:")
