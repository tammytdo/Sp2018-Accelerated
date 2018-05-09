#!/usr/bin/env python3

fruit = ["Apples, Pears, Oranges, Peaches"]

print(fruit)

response = input('What fruit do you want to add to the list?\n\n>> ')

fruit.append(response)

print(fruit)

response = input('What number fruit do you want?\n\n>> ')

print('Fruit in index, {}, is {}'.format(response, fruit[response - 1]))

fruit.insert(0, 'Mango')

print(fruit)

for name in fruit:
    if name[0].lower() == 'P':
        p_fruit.append(name)
    print(p_fruit)

copy_fruit = fruit

print(copy_fruit)

print(copy_fruit[0 : len(copy_fruit) - 1])

response = input('What fruit do you want to delete?\n\n>> ')

for i, name in enumerate(copy_fruit):
    if name == response:
        copy_fruit.pop(i)

copy_fruit = fruit

for i, name in enumerate(fruit):
    response = input('Do you like {}?\n\n>> '.format(name))
    if response.lower() == 'No':
        copy_fruit.pop(i)

print(copy_fruit)

copy_fruit = fruit

print(copy_fruit[::-1])

del fruit[-1]

print(fruit)
