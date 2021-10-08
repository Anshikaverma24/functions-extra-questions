#  Write a Python function to sum all the numbers in a list


def sum(list):
    sum=0
    i=0
    while i<len(list):
        sum=sum+list[i]
        print(sum)
        i+=1

sum([2,3,4])