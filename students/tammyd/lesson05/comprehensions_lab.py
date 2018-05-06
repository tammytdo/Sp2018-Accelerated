eggs = ['poached egg', 'fried egg']

meats = ['lite spam', 'ham spam', 'fried spam']

#can you explain this line to me? 
#it seems like it is asking to print ['egg[0] and meat[1]']
comprehension = [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

print(comprehension)


for egg in eggs:
    for meat in meats:
        print('{0} and {1}'.format(egg, meat) )