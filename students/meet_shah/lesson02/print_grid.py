def print_grid(x):
    start = "+ "
    mid   = "- "
    end   = "+"

    repeat = int(x/2)
    print(start,mid*repeat,start,mid*repeat,end)

print_grid(3)
print_grid(4)
