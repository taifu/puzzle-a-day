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
        self.ESA = ((1, 1),
                    (1, 1),
                    (1, 1))

    def rotate(self, piece):
        return tuple(tuple(row[::-1]) for row in zip(*piece))

    def reflect(self, piece):
        return tuple(tuple(row[::-1]) for row in piece)

    def get_rotations_reflections(self, piece):
        rotations_reflections = []
        rot_ref = piece[:]
        for x in range(4):
            if not rot_ref in rotations_reflections:
                rotations_reflections.append(rot_ref)
            rot_ref = self.reflect(rot_ref)
            if not rot_ref in rotations_reflections:
                rotations_reflections.append(rot_ref)
            rot_ref = self.rotate(self.reflect(rot_ref))
        return rotations_reflections

    def get_positions(self, board, piece):
        positions = []
        for y, board_row in enumerate(board):
            for x, board_cell in enumerate(board_row):
                ok = True
                for dy, piece_row in enumerate(piece):
                    for dx, piece_cell in enumerate(piece_row):
                        try:
                            if piece_cell and not board[y + dy][x + dx]:
                                ok = False
                                break
                        except IndexError:
                            ok = False
                    if not ok:
                        break
                if ok:
                    positions.append((x, y))
        return positions

    def get_matrix_rows(self, board, piece):
        positions = self.get_positions(board, piece)
        rows = []
        for px, py in positions:
            occupied = []
            for dy, piece_row in enumerate(piece):
                for dx, piece_cell in enumerate(piece_row):
                    if piece_cell:
                        occupied.append((px + dx, py + dy))
            row = []
            for y, board_row in enumerate(board):
                for x, board_cell in enumerate(board_row):
                    if board_cell:
                        row.append(1 if (x, y) in occupied else 0)
            rows.append(tuple(row))
        return(rows)

    def get_matrix_all_rows(self, board, piece, left_part_row=None):
        rows = []
        for piece in self.get_rotations_reflections(piece):
            positions = self.get_positions(board, piece)
            for px, py in positions:
                occupied = []
                for dy, piece_row in enumerate(piece):
                    for dx, piece_cell in enumerate(piece_row):
                        if piece_cell:
                            occupied.append((px + dx, py + dy))
                row = []
                for y, board_row in enumerate(board):
                    for x, board_cell in enumerate(board_row):
                        if board_cell:
                            row.append(1 if (x, y) in occupied else 0)
                rows.append((left_part_row or ()) + tuple(row))
        return(rows)

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
        pieces = (self.ESA, Pentomino.L, Pentomino.N, Pentomino.P, Pentomino.U, Pentomino.V, Pentomino.Y, Pentomino.Z)

        # 0) Scrivere l'header con tutti i pezzi
        #TODO

        # 1) Calcolare tutti i possibili piazzamenti nella board di tutte le
        # rotazioni e riflessioni dei pezzi
        #TODO

        #    1.1) Per tutti i pezzi, prendere get_matrix_all_rows
        #         e aggiungere la parte sinistra ad ogni riga (per i pezzi)
        rows = []
        for n, piece in enumerate(pieces):
            left_part_row = tuple(1 if m == n else 0 for m in range(len(pieces)))
            rows.extend(self.get_matrix_all_rows(board, piece, left_part_row))

        # 2) Costruire gli oggetti per l'algoritmo Dancing Links
        #TODO

        # 3) Cercare la soluzione e stamparla
        #TODO

        print(day, month)
