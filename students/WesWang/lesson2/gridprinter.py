def draw_floor(rowcol, size):
  for x in range(rowcol):
      print("+" + "-"*size, end='')
  print("+")

def print_grid(rowcol, size):
  for y in range(rowcol):
    draw_floor(rowcol, size)
    for wall in range(size):
      print(("|"+" "*size)*rowcol + "|")
  draw_floor(rowcol, size)


print_grid(5,4)