# Find the number of Vowels is present in sentence or word.
user_input = input("Any sentence or word: ")
variable = ['a','e',"i","o","u"]
count = 0
for i in user_input:
    if i in variable:
        count += 1      
print(count)  

