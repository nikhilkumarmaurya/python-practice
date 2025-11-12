#sorting without sort method
a = [1,3,4,3,6,5,5,3,4,344]
b = []
for i in range(len(a)):
    c = min(a)
    b.append(c)
    a.remove(c)
print(b)

#find index without index method
a = [1,3,4,3,6,5,5,3,4,344]
b = int(input("num: "))
for i in range(len(a)):
    if b == a[i]:
        print(i)
        break

#find unique obj, index, frequency
a = [1,3,4,3,6,5,5,3,4,344]
b,c,e=[],[],[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
        d = 0
        f =[]
        for j in range(len(a)):
            if a[i] == a[j]:
                d+=1
                f.append(j)
                
        c.append(d)
        e.append(f)    
for k in range(len(b)):
    print(f"Num: {b[k]} & Fre: {c[k]} & Index: {e[k]}")

#ascending descending
a = input("num: ")
print(f"Ascending: {"".join(sorted(list(a)))}\nDecending: {"".join(sorted(list(a),reverse=True))}")

# Note: Run all project at different-different section.
