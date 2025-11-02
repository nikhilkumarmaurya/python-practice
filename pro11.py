def dtob(a):
 b = ''
 c = ""
 while True:
    if a==0 or a==1:
        b+=str(a)
        break
    else:
        b+=str(a%2)
        a//=2       
 for i in range(1,(len(b)+1)):
    c+=str(b[-i])
 print("Binary No: ",c)
dec = int(input("Dec No.: ")) 
dtob(dec)
