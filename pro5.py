import random
opt = ["Stone","Paper","Kaichee"]
print('Lets start Stone Paper Secior game-')
while True:
 try:
    com = random.randint(1,3)
    ask = int(input('1.Stone\n2.Paper\n3.Secior\n4.Exit\nYour Choice: '))
    if ask == 4:
      print("bye bye")
      break
    else:
     print(f"Your Choice: {opt[ask-1]}")
     print(f"Your Choice: {opt[com-1]}")
     if ask == com :
	      print (">>>> Draw <<<<")
     elif (com == 1 and ask == 2) or (com == 2 and ask == 3) or (com == 3 and ask == 1):
      	 print (">>>> User win <<<<")
     else:
       print(">>>> computer win <<<<")
     print("-----------------------")
     print('Lets play once more -')
 except:
     print("Invalid Choice\n☆☆☆☆☆☆☆☆☆☆☆☆☆\nChoose Again-(1,2,3)")
     
		
	 
