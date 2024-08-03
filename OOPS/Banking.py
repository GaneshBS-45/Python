class Banking:
    def __init__(self,acc_no:int,name:str,acc_type:int,balance:int=0,branch:str):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
        self.branch=branch

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
    choice =input("Enter your choice")
    

