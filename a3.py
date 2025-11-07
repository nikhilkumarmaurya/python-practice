class bank :
    def __init__(self,nam,bal,acc):
        self.nam= nam
        self.bal= bal
        self.acc = acc
    def show(self):
        print(f"~~~~~~~~~~~~~\nName: {self.nam}\nBalance: {self.bal}\nAccount No: {self.acc}\n~~~~~~~~~~~~~~")

    def cre(self,cr):
        self.bal += cr
    def deb(self,deb):
        self.bal-= deb
ban = {}
while True:
 try:
  ask = int(input("\n1. Create account\n2. Check balance\n3. Debit\n4. Credit\n5. Exit\nOption: "))
  if ask == 1: 
   name = input("name: ")
   bala = int(input("Amo.:"))
   acc = int(input("Acc no.:"))
   if acc not in ban:
    ban[acc] = bank(name,bala,acc)
    ban[acc].show()
   else:
       print("User already have")
  elif ask == 2:
   acc = int(input("Acc no.:"))
   if acc in ban:
    ban[acc].show()
   else:
      print("User not found") 
  elif ask == 3:
   acc = int(input("Acc no.:"))
   if acc in ban:
    bala = int(input("Amo.:"))      
    ban[acc].deb(bala)
    print("Saved")
   else:
      print("User not found")
  elif ask == 4:
   acc = int(input("Acc no.:"))
   if acc in ban:
    bala = int(input("Amo.:"))
    ban[acc].cre(bala)
    print("Saved")
   else:
      print("User not found")
  elif ask == 5:
     print("Bank looted\nAll Data Deleted")     
     break
  else:
     print("Wrong Option")
 except:
     print("Only Number Allowed")
