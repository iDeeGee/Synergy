from utils import RandBool
from utils import RandCell
from utils import RandNextCell

# 0 - field
# 1 - tree
# 2 - river
# 3 - hospital
# 4 - upgrade shop

CELL_TYPES = "🟩🌲🟦🏥🏦"

class Map:
    def GenerateRiver(self, lenght):
        rc = RandCell(self.width, self.height)
        rx, ry = rc[0], rc[1] 
        self.cells[rx][ry] = 2
        while lenght > 0:
            rc2 = RandNextCell(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.CheckBounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                lenght -= 1


    def GenerateForest(self, r, mxr):
        for ri in range(self.height):
            for ci in range(self.width):
                if RandBool(r, mxr):
                    self.cells[ri][ci] = 1


    def PrintMap(self):
        print("⬛" * (self.width + 2))
        for row in self.cells:
            print("⬛", end="")
            for cell in row:
                if (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("⬛")
        print("⬛" * (self.width + 2))   

    def CheckBounds(self, x, y):
        if(x < 0 or y < 0 or x >= self.height or y >=self.width):
            return False
        return True

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]
 
# Тест
tmp = Map(20,10)
tmp.GenerateForest(3,10)
tmp.GenerateRiver(10)
tmp.GenerateRiver(10)
tmp.GenerateRiver(10)
tmp.PrintMap()