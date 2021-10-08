# Python function that takes a list and returns a new list with unique elements of the first list.
def unique(list):
    new=set(list)
    print(new)

unique([2,2,3,4,3,2,3,4])