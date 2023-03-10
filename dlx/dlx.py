class Dlx:
    def ones(self, row):
        return [n for n, one in enumerate(row) if one]

    def cols(self, Y, n):
        return set([col for col, row in Y.items if n in row])
        return [n for n, one in enumerate(row) if one]

    def __init__(self, header, matrix):
        import pdb; pdb.set_trace()
        assert len(header) == len(matrix)
        self.matrix = matrix
        self.Y = dict((col, self.ones(matrix[n])) for n, col in enumerate(header))
        self.X = dict((n, self.cols(self.Y, n)) for n in range(len(matrix[0])))
        import pdb; pdb.set_trace()
        self.build_structures()

    def build_structures(self):
        self.columns = []
