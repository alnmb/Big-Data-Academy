my_list = [1,4,9,16,25,36,49,64,81,100]

sliced = my_list[1:9]
odds = []
for odd in sliced:
    if odd % 2 == 0:
        odds.append(odd)
        
print (odds)