from datetime import datetime
class BankAccount:
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
        self.transaction=[]
    def record_transaction(self,transaction_type,amount):
        try:
            transaction={
                "type":transaction_type,
                "amount":amount,
                "date":datetime.now().strftime("%Y-%M-%D %H:%M:%S")
            }
            self.transaction.append(transaction)
        except Exception as e:
            print("Error during transaction")
    def deposit(self,amount):
        try:
            if amount>0:
                self.balance+=amount
                self.record_transaction("Deposit",amount)
                print(f"Deposited amount ${amount} into account {self.account_number}. new balance {self.balance}")
            else:
                print("Deposit amount must be positive")
        except Exception as e:
            print("Error during deposit:{e}")
    def withdraw(self,amount):
        try:
            if 0<amount<=self.balance:
                self.balance-=amount
                self.record_transaction("Withdrawal",amount)
                print(f"Withdrawal amount ${amount} into account {self.account_number}.new balance {self.balance}")
            else:
                print("Insufficiend balance or invalid amount")
        except Exception as e:
            print("Error during withdrawal:{e}")
    def transfer(self,target_Account,amount):
        try:
            if 0<amount<=self.balance:
                self.withdraw(amount)
                target_Account.deposit(amount)
                print(f"Transfered amount ${amount} to {target_Account.account_number} successfully")
            else:
                print("Insufficient amount")
        except Exception as e:
            print("Error during transfer:{e}")
    def showtransaction(self):
        try:
            print(f"Transaction history for account:{self.account_number}")
            for txn in self.transaction:
                print(f"{txn['date']} - {txn['type']} - {txn['amount']}")
        except Exception as e:
            print("Error during displaying transaction:{e}")
    def to_dict(self):
        return {
            "accountnumber":self.account_number,
            "accountholder":self.account_holder,
            "balance":self.balance,
            "transaction":self.transaction
        }

            