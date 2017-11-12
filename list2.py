zoo_animals = ['elephant', 'zebra', 'tiger', 'lion']

#add to the 5th element the item cheetah display the number of list items and print the new list

zoo_animals.append('cheetah')
print(zoo_animals)

#Write an assignment statement that will replace the item that currently
#holds the value "lion" in the zoo_animals list with another animal.

newAnimal = 'dog'
zoo_animals[3] = newAnimal
print(zoo_animals)

#From the list remove "zebra"
zoo_animals.pop(1)
print(zoo_animals)