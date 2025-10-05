class Account:
    def __init__(self,accnumber,accbalance,securitycode):
        self.__accnumber=accnumber
        self.__accbalance=accbalance
        self.__securitycode=securitycode

    def getinfo(self):
        print("Account Number:",self.__accnumber)
        print("Account balance:",self.__accbalance)
        print("Account security code:",self.__securitycode)

    def setinfo(self,accnumber,accbalance,securitycode):
        self.__accnumber=accnumber
        self.__accbalance=accbalance
        self.__securitycode=securitycode

Acc=Account("XYZ",20000,3456)
Acc.setinfo("WXYZ",30000,78654)
Acc.getinfo()



        