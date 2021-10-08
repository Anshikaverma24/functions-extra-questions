# Write a Python function to find the Max of three numbers
def max():
    num1=int(input("enter 1st no."))
    num2=int(input("enter 2nd no."))
    num3=int(input("enter 3rd no."))
    if num1>num2 and num1>num3:
        print("GREATER NUMBER - ", num1)
    elif num2>num1 and num2>num3:
        print("GREATER NUMBER - ", num2)
    elif num3>num1 and num3>num2:
        print("GREATER NUMBER - ", num3)


max()