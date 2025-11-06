# Password Generater based on secret key and username so that you will not forget it.
while True:
    try:
       us = []
       sym = ["%","#","@","!","₹,","#"]
       print("Welcome to the Password Generater\n1.Start\n2.Exit")
       ask = int(input("Option: "))
       if ask == 1:
           username = input("Username: ")
           sec = input("Write one word: ")
           half = len(sec)//2
           while True:
             if len(sym) < len(username):
              sym.append(sym)
             else:
                 break
           for i in range(len(username)-1):
              us.append(username[i])
              us.append(sym[i])
           us.reverse()
           print(f"Your password: {sec[half:len(sec)]}{"".join(us)}{sec[0:half]}")   
       elif ask == 2:
           print("Thanks for use")
           break
       else:
          print("Invalid")    
       print()          
    except:
         print("Invalid")
         print()
