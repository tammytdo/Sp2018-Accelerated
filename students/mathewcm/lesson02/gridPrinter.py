def beam():
    """
    beam() function defines one of three beams in a 2x2 grid pattern
    """
    print("+----+----+", end=" ")

def post():
    """
    post() function defines one of eight posts separating and propping up the beams in a 2x2 grid pattern
    """
    print("|     |     |", end=" ")

def printGrid():
    """
    printGrid() function calls the beam() function then four post() functions then another beam, then four more post() functions then a final beam() to complete a 2x2 grid
    """
    beam()
    post()
    post()
    post()
    post()
    beam()
    post()
    post()
    post()
    post()
    beam()

def beamFunc(width):
    """
    beamFunc() function prints 'width' number of beams wide.
    """
    print(" + ----"*width,"+")

def postFunc(width):
    """
    postFunc(p) prints 'width' number of posts wide.
    """
    print(" |     "*width, "|")

#Need to dry code and replace length and width to just a 'units' that is length times height.

def print_fill(horizontal, fill = ' ', rowXcolumn = 2, units = 2):
    """
    def print_fill(horizontal, fill = ' ', units = 2):
        where 'horizontal' is the horizontal line which makes up the 'fill' times the parameter units. The function loops through and prints the horizontals fill 'units' number of times.
    """
    for i in range(units):
        print("%s %s " % (horizontal, fill*units), end="")
    print(horizontal)

def draw_grid(rowXcolumn = 2, units = 2):
    """
    draw_grid() loops thru printing a grid determined by the parameters units and rowXcolumn.
    """
    for j in range(units):
        print_fill('+', '-', rowXcolumn, units)
        for k in range(rowXcolumn):
            print_fill('|', ' ', rowXcolumn, units)
    print_fill('+', '-', rowXcolumn, units)
