# 0 - field
# 1 - tree
# 2 - river
# 3 - hospital
# 4 - upgrade shop
class Map:
    #def GenerateRivers():

    #def GenerateForest():

    def PrintMap(self):
        for row in self.cells:
            for cell in row:
                if cell == 0:
                    print("🟩", end="")
                elif cell == 1:
                    print("🌲", end="")
                elif cell == 2:
                    print("🌊", end="")
                elif cell == 3:
                    print("🏥", end="")
                elif cell == 4:
                    print("🏦", end="")
            print()        

    def __init__(self, width, height):
        self.cells = [[0 for i in range(width)] for j in range(height)]

# tmp = Map(10,10)
# tmp.cells[1][1] = 1
# tmp.cells[2][2] = 2
# tmp.PrintMap()        