from utils import RandBool
from utils import RandCell
from utils import RandNextCell

# 0 - field
# 1 - tree
# 2 - river
# 3 - hospital
# 4 - upgrade shop
# 5 - fire

CELL_TYPES = "🟩🌲🟦🏥🏦🔥"
TREE_BONUS = 100
#TODO: change 5000
UPGRADE_COST = 300
#TODO: change 10000
LIFE_COST = 500

class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]
        self.GenerateForest(3,10) # 3,10
        self.GenerateRiver(10)
        self.GenerateRiver(10)
        self.GenerateRiver(10)
        self.UpgradeShop()
        self.Hospital()

# SYSTEM
    def PrintMap(self, helico, clouds):
        """
        Вывод тайлов карты
        """
        print("⬛" * (self.width + 2))
        for ri in range(self.height):
            print("⬛", end="")
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print("*", end="")
                elif (clouds.cells[ri][ci] == 2):
                    print("$", end="")
                if (helico.x == ri and helico.y == ci): # был if
                    print("🚁", end="")
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("⬛")
        print("⬛" * (self.width + 2))   

    def CheckBounds(self, x, y):
        """
        Проверка заполнения 
        """
        if(x < 0 or y < 0 or x >= self.height or y >=self.width):
            return False
        return True        
# RIVER
    def GenerateRiver(self, lenght):
        """
        Генерация рек
        """
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

# FOREST & TREE
    def GenerateForest(self, r, mxr):
        """
        Генерация леса
        """
        for ri in range(self.height):
            for ci in range(self.width):
                if RandBool(r, mxr):
                    self.cells[ri][ci] = 1

    def AddTree(self):
        """
        Добавление нового дерева на поле
        """
        c = RandCell(self.width, self.height)
        cx, cy = c[0], c[1]
        if(self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

# FIRE
    def AddFire(self):
        """
        Добавление огня на дерево
        """        
        c = RandCell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5 

    def UpdateFires(self):
        for ri in range(self.height):
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if cell == 5:                    
                    self.cells[ri][ci] = 0
        for i in range(10):
            self.AddFire() 

# UPGRATE & HEALTH
    def UpgradeShop(self):
        c = RandCell(self.width, self.height)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def Hospital(self):
        c = RandCell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.Hospital()

    

# PROC HELICOPTER
    def ProcessHelicopter(self, helico):
        c = self.cells[helico.x][helico.y] 
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 5  and helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if (c == 4 and helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if (c == 3 and helico.score >= LIFE_COST):
            helico.lives += 1
            helico.score -= LIFE_COST