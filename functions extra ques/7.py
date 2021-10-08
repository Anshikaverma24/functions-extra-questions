# Write a Python program to print the even numbers from a given list. Go to the editor

def even(list):
    i=0
    while i<len(list):
        if list[i]%2==0:
            print("EVEN NUMBER - ", list[i])
        i+=1

even([2,3,4,5,6,7])