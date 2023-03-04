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


class Board:
    """
     0   1   2   3   4   5
   +-----------------------+
 0 |Jan|Feb|Mar|Apr|May|Jun|
   +---+---+---+---+---+---+
 1 |Jul|Aug|Sep|Oct|Nov|Dec| 6
   +---+---+---+---+---+---+---+
 2 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
   +---+---+---+---+---+---+---+
 3 | 8 | 9 | 10| 11| 12| 13| 14|
   +---+---+---+---+---+---+---+
 4 | 15| 16| 17| 18| 19| 20| 21|
   +---+---+---+---+---+---+---+
 5 | 22| 23| 24| 25| 26| 27| 28|
   +---+---+---+---+---+---+---+
 6 | 29| 30| 31|
   +-----------+

   +-----------------------+
   |0,0|1,0|2,0|3,0|4,0|5,0|
   +---+---+---+---+---+---+
   |0,1|1,1|2,1|3,1|4,1|5,1|
   +---+---+---+---+---+---+---+
   |0,2|1,2|2,2|3,2|4,2|5,2|6,2|
   +---+---+---+---+---+---+---+
   |0,3|1,3|2,3|3,3|4,3|5,3|6,3|
   +---+---+---+---+---+---+---+
   |0,4|1,4|2,4|3,4|4,4|5,4|6,4|
   +---+---+---+---+---+---+---+
   |0,5|1,5|2,5|3,5|4,5|5,5|6,5|
   +---+---+---+---+---+---+---+
   |0,6|1,6|2,6|
   +-----------+
   """

    def __init__(self):
        self.board = ((1, 1, 1, 1, 1, 1, 0), # Month Jan-Jun
                      (1, 1, 1, 1, 1, 1, 0), # Month Jul-Dec
                      (1, 1, 1, 1, 1, 1, 1), # Day 1-7
                      (1, 1, 1, 1, 1, 1, 1), # Day 8-14
                      (1, 1, 1, 1, 1, 1, 1), # Day 15-21
                      (1, 1, 1, 1, 1, 1, 1), # Day 22-28
                      (1, 1, 1, 0, 0, 0, 0), # Day 29-31
                      )
        self.pieces = Pentomino()

    def rotate(self, piece):
        return tuple(tuple(row[::-1]) for row in zip(*piece))

    def reflect(self, piece):
        return tuple(tuple(row[::-1]) for row in piece)

    def get_date(self, day, month):
        board = []
        for i, row in enumerate(self.board):
            row = list(row)
            if i == 0:
                if month < 7:
                    row[month - 1] = 0
            elif i == 1:
                if month > 6:
                    row[month - 7] = 0
            else:
                if (i - 2) * 7 <= day - 1 < (i - 1) * 7:
                    row[(day - 1) % 7] = 0
            board.append(tuple(row))
        return tuple(board)

    def solve(self, day, month):
        board = self.get_date(day, month)
        # 1) Calcolare tutti i possibili piazzamenti nella board di tutte le
        # rotazioni e riflessioni dei pezzi
        # 2) Costruire gli oggetti per l'algoritmo Dancing Links
        # 3) Cercare la soluzione e stamparla
        print(day, month)
