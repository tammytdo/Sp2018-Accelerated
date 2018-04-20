
plus = "+"
minus = "-"
space = " "
post = "|"
block = (space + minus + space + minus + space +
     minus + space + minus + space)


def topmidbot():
    print(plus + block + plus + block + plus)


def postline():
    print(post + space * 9 + post + space * 9 + post)
    print(post + space * 9 + post + space * 9 + post)
    print(post + space * 9 + post + space * 9 + post)
    print(post + space * 9 + post + space * 9 + post)


topmidbot()
postline()
topmidbot()
postline()
topmidbot()
