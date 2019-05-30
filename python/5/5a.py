class WithdrawalError(Exception):
    pass
class DepositError(Exception):
    pass
class SavingsAccount:
    def __init__(self,b=500):
        try:
            if b<500:
                raise DepositError
            else:
                self.bal=b
                print('Account created with balance:',self.bal,'\n')
        except DepositError:
            print('Minimum amount to be deposited to create an account is 500.Please deposit Rs.500.\n')
            del(self)
    def deposit(self,a):
        self.bal+=a
        print('Rs.',a,'has been deposited. Your available balance:',self.bal,'\n')
    def withdraw(self,x):
        try:
            if x>self.bal:
                raise WithdrawalError
            else:
                self.bal-=x
                print('Rs.', x, 'has been withdrawn. Your available balance:', self.bal, '\n')
        except WithdrawalError:
            print('You cannot withdraw more than the account balance. Available balance:',self.bal)
u=SavingsAccount(400)
u=SavingsAccount(1000)
u.deposit(10000)
u.withdraw(200000)
u.withdraw(2000)
