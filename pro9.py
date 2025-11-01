while True:
 a = input("\nFull name: ")
 if a.replace(" ","").isalpha():
  if a.isalpha():
    print(a.upper())
  else:
    for i in range(len(a)-1,0,-1):
        if a[i] == ' ':
            break
    print(a[0].upper(),end='.')
    for j in range(0,i):
        if a[j] == ' ':
            print(a[j+1].upper(),end='.')
    print(a[i+1:].upper(),end='')
 else:
  print("Invalid Input") 
  
