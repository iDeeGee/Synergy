from utils import RandBool

class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def UpdateClouds(self, r, mxr, g = 4, mxg = 10):
        for i in range(self.h):
            for j in range(self.w):
                if RandBool(r, mxr):
                    self.cells[i][j] = 1
                    if RandBool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0