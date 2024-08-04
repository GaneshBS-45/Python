class Banking:
    def __init__(self,acc_no:int,name:str,acc_type:str,branch:str,balance:int=0):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
        self.branch=branch

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
         if self.balance>=amount:
            self.balance-=amount

    def transfer(self, target_acc, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            target_acc.deposit(amount)
        else:
            print("Insufficient balance for transfer")

    def display(self):
        print(f"self acc_no {self.acc_no}")
        print(f"self name {self.name}")
        print(f"self acc_type {self.acc_type}")
        print(f"self balance {self.balance}")
        print(f"self branch {self.branch}")

bank_account=[]

while True:
    print("1)add an account")
    print("2)Display all account")
    print("3)deposit money")
    print("4)withdraw the money")
    print("5)tranfer the account")
    print("6) exit")

    Choice =int(input("Enter your choice = "))

    if Choice==1:
        acc_no=int(input("Enter your Account number ="))
        name=(input("Enter your name ="))
        acc_type=str(input("Enter your accnt_type number ="))
        branch=str(input("Enter your branch number ="))
        balance=int(input("Enter your balance ="))
        acc1=Banking(acc_no,name,acc_type,branch,balance)
        bank_account.append(acc1)
    elif Choice==2:
        if len(bank_account)>0:
            for acc in bank_account:
                acc.display()
        else:
            print("please add the accounts")
    elif Choice==3:
        account_no=int(input("please enter your account number ="))
        for acc in bank_account:
            if acc.acc_no==account_no:
                amt=int(input("Enter the amount to deposit ="))
                acc.deposit(amt)
    elif Choice==4:
        account_no=int(input("please enter your account number ="))
        for acc in bank_account:
            if acc.acc_no==account_no:
                amt=int(input("Enter the amount to be debited ="))
                acc.withdraw(amt)
                break
        else:
            print("enter the correct account no")
    elif Choice==5:
        accnt_no1=int(input("Enter the account number to debit="))
        accnt_no2=int(input("Enter the account number to deposit="))
        from_acc=None
        to_acc=None
        for acc in bank_account:
            if acc.acc_no==accnt_no1:
                from_acc=acc
            if acc.acc_no==accnt_no2:
                to_acc=acc
        
        if from_acc and to_acc:
            print("inside the transfer stage")
            amnt=int(input("Enter the amount to be transfered ="))
            # from_acc.display()
            from_acc.withdraw(amnt)
            to_acc.deposit(amnt)         
    elif Choice==6:
        break
    else:
        print("Invalid choice")

    

    

