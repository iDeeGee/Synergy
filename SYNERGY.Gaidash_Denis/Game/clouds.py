from utils import RandBool

# 0 - empty
# 1 - normal cloud
# 2 - lighting cloud

class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def UpdateClouds(self, r = 2, mxr = 10, g = 4, mxg = 10):
        for i in range(self.h):     #self.h
            for j in range(self.w): #self.w
                if RandBool(r, mxr):
                    self.cells[i][j] = 1
                    if RandBool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0