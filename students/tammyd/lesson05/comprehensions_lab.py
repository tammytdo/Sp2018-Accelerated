dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

print(dict_comprehension)

print(len(dict_of_weapons))
print(len(dict_comprehension))