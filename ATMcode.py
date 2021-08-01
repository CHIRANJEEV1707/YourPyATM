class ATM:
          def __init__(self,cardNo,pin,balance):
                    self.cardNo=cardNo
                    self.pin=pin
                    self.balance=balance

          def checkBalance(self):
                    print("WELCOME TO CHI BANK!!!")
                    print("YOUR ONE STOP SOLUTION TO ALL FINANCIAL PROBLEMS!!!")
                    print("current balance=",self.balance)
          def checkWithdrawal(self,amount):
                    x=50000-amount
                    print("remaining balance=",x)
                    print("HAVING TROUBLES WITH YOUR ACCOUNT CONTACT YOUR BANK MANAGER!!!")
                    print("LOOKS LIKE YOU EARNED LESS PROFIT, CHECK OUR SCHEMES AND INCREASE YOUR PROFIT UPTO 3 TIMES!!!")

CU1=ATM("RE001",1234,50000)       
CU1.checkBalance()  
CU1.checkWithdrawal(10000)           
              