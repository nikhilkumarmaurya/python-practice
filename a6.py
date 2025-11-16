# Table generater form to to.
num1 = int(input("From: "))
num2 = int(input("To: "))
table = [i for i in range(num1,num2+1)]
for i in range(len(table)):
    for j in range(1,11):
        print(table[i]*j,end=" ")
    print()
