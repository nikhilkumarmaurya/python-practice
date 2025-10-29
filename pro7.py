def factorial(num):           
        if num == 1:
            return 1
        else:
            return num*factorial(num-1)
            
while True:
 try:
  print(f"Factorial is {factorial(int(input("Factorial of: ")))}")
  break
 except:
    print("Invalid Input")
