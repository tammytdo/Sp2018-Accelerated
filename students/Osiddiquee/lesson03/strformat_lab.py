
filestuff = (2, 123.4567, 10000, 12345.67)
(w, x, y, z) = filestuff


#task 1
def filename_generator(filename, first, second, third):
    return 'file_00{:d}: {:10.2f}, {:.2e}, {:.2e}'.format(filename,
                                                          first,
                                                          second,
                                                          third)

print(filename_generator(w, x, y, z))


#task 2
def alt_filename_generator(filename, first, second, third):
    return f'file_00{filename}: ' + '{:10.2f}, {:.2e}, {:.2e}'.format(first,
                                                                      second,
                                                                      third)

print(alt_filename_generator(w, x, y, z))


#task 3
tup = (1, 2, 3)
tup2 = (1, 2, 3, 4, 5)
def tuple_format(tuple):
    first_piece = f'the {len(tuple)} numbers are: '
    second_piece = '{}'
    for i in len(tuple) - 1:
        second_piece += ', {}'
    return (first_piece + second_piece).format(tuple)

print(tup)
print(tup2)


#task 4
def tuple_reorder(tuple):
    return (str(tuple[3]) + ' ' +
            str(tuple[4]) + ' ' +
            str(tuple[2]) + ' ' +
            str(tuple[0]) + ' ' +
            str(tuple[1]))

print(tuple_reorder(tup2))


#task 5
fruit_data = ['oranges', 1.3, 'lemons', 1.1]
print(f'''The weight of an {fruit_data[0]} is {fruit_data[1]}
          and the weight of a {fruit_data[2]} is {fruit_data[3]}''')


#task 6
'{:10e} + {:10e} + {:10e} + {:10e} + {:10e}'.format('First',
                                                    '$99.01',
                                                    'Second',
                                                    '$88.09')
