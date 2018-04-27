
def fibonacci(n):
    '''Return the nth value in the fibonacci series.'''
    if n == 1:
        return 0
    if n == 2:
        return 1
    else :
        return fibonacci(n-2)+fibonacci(n-1)
#fibonacci(8) ->13



def lucas(n):
    '''Returns the nth value in the lucas numbers series'''
    if n == 1:
        return 2
    if n == 2:
        return 1
    else :
        return lucas(n-2)+lucas(n-1)
#lucas(5) ->7


def sum_series(n, x=0, y=1):
    '''Returns the nth value in the series'''
    if n == 1:
        return x
    if n == 2:
        return y
    else :
        return sum_series(n-2,x,y)+sum_series(n-1,x,y)

#sum_series(5) -> 3
#sum_series(5,2,1) -> 7
