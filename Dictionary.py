#create dictionary of   names and birthdays
#display available items and ask the user for a name and return birthday

people = {'Alan': '07/31/1992',
          'Magda': '08/14/1992',
          'Amalia': '07/10/1956',
          'Alberto': '08/08/1954',
          'Erik':'08/04/1981',
          'Brenda': '05/10/1977'}

print(people.keys())

name = input('Please provide a name to display birthday: ')


if name.title() in people:
    print(people[name])
else:
    print('The provided name ', name ,' is not available')
