from random import randint as ran

# Random word selection
a = "apple game nikhil"
b = a.split()
print(b)
c = ran(0, len(b) - 1)
d = b[c]

# Randomly reveal one letter
e = ran(0, len(d) - 1)
f = d[e]

# Create hidden list
g = []
for i in d:
    if f == i:
        g.append(i)
    else:
        g.append("_")
k = " "
print("Guess the word:", k.join(g))

while True:
    ask = input("alpha: ").lower()

    if ask in d:
        for i in range(len(d)):
            if d[i] == ask:
                g[i] = ask
        print(k.join(g))
    else:
        print("Wrong guess!")

    # Check if game completed
    if  "_"  not in g:
        print("You guessed the word:", d)
        break
