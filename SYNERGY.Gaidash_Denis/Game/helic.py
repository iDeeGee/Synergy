from utils import RandCell

class Helicopter:
    def __init__(self, w, h):
        rc = RandCell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry