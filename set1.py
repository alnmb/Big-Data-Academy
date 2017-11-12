#With two given lists [1, 3, 6, 24, 78, 35, 55] and [12, 24, 35, 24, 88,120,155]
#write a program to make a list with only the elements that are in both lists.

list1 = [1, 3, 6, 24, 78, 35, 55]
list2 = [12, 24, 35, 24, 88,120,155]

finalSet = set()

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            finalSet.add(item1)

print(finalSet)