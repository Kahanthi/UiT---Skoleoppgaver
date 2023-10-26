from datetime import datetime

class Transaction:
    def __init__(self, amount):
        self.__time = self.__getTimeAsStr()
        self.__amount = amount

    def __getTimeAsStr(self):
        current_time = datetime.now()
        return current_time.strftime("%Y-%m-%d %H:%M:%S")

    def getTime(self):
        return self.__time

    def getAmount(self):
        return self.__amount

    def __str__(self):
        return f"Time: {self.__time}, Amount: {self.__amount}"