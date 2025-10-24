import random as ran
print("Welcome To Number Guessing Game")
while True:
  try:  
        fnum = int(input("From: "))
        snum = int(input("To: "))
        print("Guess the number from",fnum, "to",snum)
        if fnum > snum:
            fnum,snum = snum,fnum
        comguess = ran.randint(fnum,snum)
        print(comguess)
        break
  except:
      print("Input should be an integer\nTry Again")
count = 0
while True: 
    try:
      ask = int(input("1.Play\n2.Exit\nOptions: "))
      if ask == 1:
        count += 1
        asknum = int(input("Your Guess: "))
        if asknum > comguess:
            print("Too High")
        elif asknum < comguess:
            print("Too Low")
        else:
            print("Your guess is right that is",asknum)
            print("You take",count,"times to guess right.")
      else:
          print("---Game---")
          break
        
    except: 
        print("invalid")
        continue
    

    
 
 
