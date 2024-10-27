from functools import reduce

def getCount(listOfElems, cond=None):
    if cond:
        count = sum(1 and (elem) for elem in listOfElems if cond(elem))
    else:
        count = len(listOfElems)
    return count

def main():
    listOfElems = [11, 22, 33, 45, 66, 77, 88, 99, 101]
    print("**** Example 1: Use map() & sum() to count elements in list that satisfy certain conditions ****")
    count = sum(map(lambda x: x % 2 == 1, listOfElems))
    print("Count of odd numbers in a list:", count)
    count = sum(map(lambda x: x % 2 == 0, listOfElems))
    print("Count of even numbers in a list:", count)
    count = sum(map(lambda x: x > 5, listOfElems))
    print("Count of numbers in a list which are greater than 5:", count)
    print("**** Using sum() & Generator expression to count elements in list based on conditions ****")
    count = getCount(listOfElems, lambda x: x > 5)
    print("Count of numbers in a list which are greater than 5:", count)
    count = getCount(listOfElems, lambda x: x > 5 and x < 20)
    print("Count of numbers in a list which are greater than 5 but less than 20:", count)
    count = getCount(listOfElems)
    print("Total number of elements in list:", count)
    print("**** Use list comprehension to count elements in list based on conditions ****")
    count = len([elem for elem in listOfElems if elem > 5])
    print("Count of numbers in a list which are greater than 5:", count)
    print("**** Use reduce() function to count elements in list based on conditions")
    count = reduce(lambda default, elem: default + (elem > 5), listOfElems, 0)
    print("Count of numbers in a list which are greater than 5:", count)

if __name__ == "__main__":
    main()
