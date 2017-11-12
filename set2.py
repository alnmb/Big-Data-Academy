#Delete the 'Sloth' and 'Bengal Tiger' items from zoo_animals using del.

#Set the value associated with 'Rockhopper Penguin’ to anything other than 'Arctic Exhibit'.

zoo_animals = {'Unicorn': 'Cotton Candy House',
               'Sloth': 'Rainforest Exhibit',
               'Bengal Tiger': 'Jungle House',
               'Atlantic Puffin': 'Arctic Exhibit',
               'Rockhopper Pinguin': 'Arctic Exhibit'}

del zoo_animals['Sloth']
print(zoo_animals)

zoo_animals['Rockhopper Pinguin']  = 'Entrance'
print(zoo_animals)
