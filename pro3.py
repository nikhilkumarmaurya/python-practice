while True:
    print("----------------")
    print("What you want to do?\n1. Encode Message\n2. decode Message")
    ask = int(input("No.: "))
    if ask == 1:
# encoding
     print("----------------")
     ask = input("Your Message: ")
     a = ask[::-1] # lihkin
     b = len(a) # 6
     c = b//2 # 3
     d = a[:c] # lin
     e = a[c:] # kih
     f = e+d  # kinlih
     print("v-------v--------v")
     print(f"Your encripted message: {f}")
    elif ask == 2:
        
# Decoding
     print("Note: If you app not support clipboard then direct paste the encripted message on code.\n")
     f = input("Your encripted Message: ")
     g1 = f[::-1] # hilnik
     h = len(f) # 6
     i = h//2 # 3
     j = g1[:i] # hil
     k = g1[i:] # nik
     l = k+j
     print(l)
    else:
        print("Invalid Number")








