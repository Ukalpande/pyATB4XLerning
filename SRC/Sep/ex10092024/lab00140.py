# Custom exception - own exception

class BalanceLowException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW"))
if withdraw > balance:
    raise BalanceLowException(" balance is low !!")

else:
    print("REMAIN BAL", (balance- withdraw))