from Transactions import Transaction

class Account:
    def __init__(self, custID, accountNo, balance, interest):
        self.__custID = custID
        self.__accountNo = accountNo
        self.__balance = balance
        self.__interest = interest
        self.__transactions = []

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            transaction = Transaction(amount)
            self.__transactions.append(transaction)
        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount > 0:
            self.__balance -= amount
            transaction = Transaction(-amount)
            self.__transactions.append(transaction)
        return self.__balance

    def showTransactions(self):
        for transaction in self.__transactions:
            print(transaction)

    def __str__(self):
        return f"Customer ID: {self.__custID}, Account Number: {self.__accountNo}, Balance: {self.__balance}, Interest: {self.__interest}"