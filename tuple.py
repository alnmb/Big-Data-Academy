#Write a program to generate and print another tuple whose values are
#even numbers in the given tuple:
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).
#Output:
#(2, 4, 6, 8, 10)

number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
number_list = []

for item in number_tuple:
    if item % 2 == 0:
        number_list.append(item)

print(number_list)
