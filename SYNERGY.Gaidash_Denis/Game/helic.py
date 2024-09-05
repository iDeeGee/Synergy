from utils import RandCell

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

    def Move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def PrintStats(self):
        print("🔵 ", self.tank,"/",self.mxtank, sep="", end=" | ")
        print("🏆")