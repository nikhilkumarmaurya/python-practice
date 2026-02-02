class bank:
    def __init__(self,amo,pas):
        self.__amo = amo
        self.__pas = pas
    def dep(self,amou):      
            self.__amo += amou
            print(f"{amou} is deposited.\nYour total balance is {self.__amo}")
    def wit(self,amou,passw):
        if passw == self.__pas and self.__amo >= amou:
            self.__amo -= amou
            print(f"{amou} is withdraw.\nYour total balance is {self.__amo}")
        else:
            print("Wrong Password")
    def che(self,passw):
        if passw == self.__pas:
             print(f"Your total balance is {self.__amo}")
        else:
             print("Wrong Password")
    def sen(self,amou,passw,acc):
        if passw == self.__pas and self.__amo >= amou:
            acc.dep(amou)
            self.__amo -= amou
            print(f"{amou} is transferred.\nYour balance is {self.__amo}")
        else:
            print("Wrong formet or password or less amount.")            
     
a = bank(500,0)
b = bank(700,1)
b.che(1)
a.che(0)
a.sen(400,0,b)
