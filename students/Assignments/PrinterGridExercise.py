#Upload to GIT Test

plus = '+'

minus = '-'

line = '|'

space = ' '


def print_grid(n):
    yolo = ((n-1)//2)
    row = (plus+minus*yolo+plus+minus*yolo+plus)
    column = (line+space*yolo+line+space*yolo+line)
    print(row)
    print(column)
    print(row)
    print(column)
    print(row,end='')

print_grid(3)

