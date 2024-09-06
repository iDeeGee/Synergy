from utils import RandCell
import os

class Helicopter:
    def __init__(self, w, h):
        rc = RandCell(w, h)
        rx, ry = rc[0], rc[1]
        self.h = h
        self.w = w
        self.x = rx
        self.y = ry
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 10

    def Move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def PrintStats(self):
        print("🔵 ", self.tank,"/",self.mxtank, sep="", end=" | ")
        print("🏆", self.score, end=" | ")
        print("❤ ", self.lives)

    def GameOver(self):        
        os.system("cls")
        print("*" * 30)
        print("GAME OVER, YOUR SCORE: ", self.score)
        print()
        print("*" * 30)
        exit(0)

    def ExportData(self):
        return  {"score": self.score,
                "lives": self.lives,
                "x": self.x, "y": self.y,
                "tank": self.tank, "mxtank": self.mxtank}
    
    def ImportData(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.lives = data["lives"] or 10
        self.score = data["score"] or 0
