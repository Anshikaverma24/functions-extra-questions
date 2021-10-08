# 3. Write a Python function to multiply all the numbers in a list
# Sample List : (8, 2, 3, -1, 7)

def mul(list):
    mul=1
    i=0
    while i<len(list):
        mul=mul*list[i]
        print(mul)
        i+=1

mul([2,2,2])