class Matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[None for _ in range(m)] for _ in range(n)]

    def __str__(self):
        disp = ''
        for a in self.data:
            disp += '\n'
            for n in a:
                disp += '[%s]' % n
        return 'Matrix (%s x %s):%s' % (self.n, self.m, disp)

    def zeros(self):
        for a in range(self.n):
            for b in range(self.m):
                self.data[a][b] = 0
        return self

    def setTo(self, data):
        if len(data) == self.n:
            for line in data:
                if len(line) != self.m:
                    return False
            self.data = data
            return self

    def setElem(self, n, m, val):
        self.data[n][m] = val

    def getElem(self, n, m):
        return self.data[n][m]

    def multiply(self, othr):
        res = Matrix(self.n, othr.m).zeros()
        for an in range(self.n):
            for bm in range(othr.m):
                s = 0
                for p in range(self.m):
                    st = self.getElem(an, p) * othr.getElem(p, bm)
                    s += st
                res.setElem(an, bm, s)
        return res
