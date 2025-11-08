class sem:
    def __init__(self,name,rnum,amo):
        self.name = name
        self.rnum= rnum
        self.amo = amo
    def show(self):
        print(f"{"*"*10}\nNAME : {self.name}\nROLL NUMBER : {self.rnum}\nAMOUNT : {self.amo}\n{"*"*10}")        
    def cr(self,cre):
        self.amo+= cre
data ={}
tfee = 12500
while True:
       try:
        ask = int(input("1.new student\n2.check\n3.add amount\n4.exit\noption : "))
        if ask == 1:
            name = input("enter the student name : ")
            rnum = int(input("roll number : "))
            amo = int(input("basic amount : "))                        
            data[rnum]= sem(name,rnum,amo)
            data[rnum].show()
        elif ask == 2:
            rnum = int(input("Roll number : "))
            a = data[rnum].amo
            if a < tfee:
               print("STATUS")
               data[rnum].show()
               print("unpaid")
            else:
                print("paid")
        elif ask == 3:
            rnum = int(input("Roll number : "))
            amo = int(input("Add amount : "))
            data[rnum].cr(amo)
            data[rnum].show()
        elif ask == 4:
            print("exit")
            break
        else:
            print("invalid input")
       except:
           print("try again")
                
            
            
            
            
        

 
