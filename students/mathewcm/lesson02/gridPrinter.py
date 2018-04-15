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

#Need to dry code and replace length and width to just a 'size' that is length times height.

def print_middle(beam, middle = ' ', width = 2, length = 2):
    """
    def print_middle(beam, middle = ' ', width = 2, length = 2):
        where 'beam' is the horizontal line which makes up the 'middle' times the parameter width. The function loops through and prints the beams middle 'length' number of times.
    """
    for i in range(length):
        print("%s %s " % (beam, middle*width), end="")
    print(beam)

def draw_grid(length = 2, height = 2, width = 2):
    """
    draw_grid() loops thru printing a grid determined by the parameters width and length.
    """
    for j in range(height):
        print_middle('+', '-', width, length)
        for k in range(length):
            print_middle('|', ' ', width, length)
    print_middle('+', '-', width, length)
