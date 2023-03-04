class Pentomino:
    F = ((0, 1, 1), 
         (1, 1, 0),  
         (0, 1, 0))
    I = ((1,), 
         (1,),  
         (1,),  
         (1,),  
         (1,))
    L = ((1, 0), 
         (1, 0),
         (1, 0),
         (1, 1))  
    N = ((0, 1), 
         (1, 1),
         (1, 0),
         (1, 0))
    P = ((1, 1), 
         (1, 1),
         (1, 0))
    T = ((1, 1, 1), 
         (0, 1, 0),
         (0, 1, 0))  
    U = ((1, 0, 1), 
         (1, 1, 1))  
    V = ((1, 0, 0), 
         (1, 0, 0),
         (1, 1, 1))  
    W = ((1, 0, 0), 
         (1, 1, 0),
         (0, 1, 1))  
    X = ((0, 1, 0), 
         (1, 1, 1),  
         (0, 1, 0))
    Y = ((0, 1), 
         (1, 1),  
         (0, 1),
         (0, 1))
    Z = ((1, 1, 0), 
         (0, 1, 0), 
         (0, 1, 1))
    ESA = ((1, 1),
           (1, 1),
           (1, 1))


def date_to_array(day, month):
    """ Day: 1-31 Month: 1-12 -> (m, d) """
    assert 1 <= month <= 12
    assert 1 <= day <= 31
    return (month - 1, 11 + day)


def rotate(piece):
    return tuple(tuple(row[::-1]) for row in zip(*piece))


def reflect(piece):
    return tuple(tuple(row[::-1]) for row in piece)


def size(piece):
    return tuple(tuple(row[::-1]) for row in piece)


def solve(day, month):
    print(day, month)
