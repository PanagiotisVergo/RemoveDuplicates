#! usr/bin/env python

def removeDup(list):
    for i in list:
        if i not in new_list:
            new_list.append(i)

    print("The new list without duplicates is:", new_list)
    print("")
    sorted_list = sortList(new_list)

def sortList(list):
    list.sort()

    print("The latest list sorted is:", list)



new_list = []
list = [10, 15, 25, 10, 10, 7, 9, 13, 15]
new_list = removeDup(list)




