print("-- Expense Tracker --")
tAmo = int(input("Total Amount: "))
tExp = 0
tRem = 0
lists = []

 
def item():
    global tExp
    iName = input("Item Name: ")
    iQty = int(input("Item Quantity: "))
    iAmo = int(input("Amount/item: "))
    itAmo = iQty * iAmo
    print(f"Item Name: {iName}\nItem Quantity: {iQty}\nItem Total Amount: {itAmo}")
    tExp += itAmo
    lists.append((iName,iQty,iAmo))  
    
def iShow():
    tRem = tAmo - tExp
    for item in lists:
        print(item)
    print(f"Total Amount: {tAmo}\nTotal Expend: {tExp}\nTotal Remaining: {tRem}")

while True:
 ask = input("1.add\n2.show\nOption: ")
 if ask == '1':
   item()
   print()
 elif ask == "2":
    iShow()
    print()
 else:
   print("invalid option")  
     
