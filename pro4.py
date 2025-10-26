def hal():
 while True: 
  ask = input("Want to play (y/n): ")
  if ask == "n":
    break
  elif ask == "y":    
   try:   
    n1 = int(input("Num1: "))
    n2 = int(input("Num2: "))
    print("n1:",n1,"\nn2:",n2)
    def hcf(n1,n2):
     while True :
        rem = n1%n2
        if rem==0:
            return n2
        else:
            n1 = n2
            n2 = rem
    print("HCF:",hcf(n1,n2))
    def lcm(n1,n2):
     lcm = (n1*n2)/hcf(n1,n2)
     return lcm
    print("LCM:",lcm(n1,n2))  
   except:
     print("Value is invalid:")
     print("Ex:\n Num1 = 4\n Num2 = 2")
  else:
   print("Invalid input:",ask)
hal()
