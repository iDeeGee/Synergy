# 0 - field
# 1 - tree
# 2 - river
class Map:
    #def GenerateRivers():

    #def GenerateForest():

    def PrintMap():
        for row in self.cells:
            for cell in row:
                if cell == 0:
                    print("", end="")

    def __init__(self, width, height):
        self.cells = [[0 for i in range(width)] for j in range(height)]