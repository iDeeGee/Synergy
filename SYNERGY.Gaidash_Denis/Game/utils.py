from random import randint as rand

def RandBool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

def RandCell(w, h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return(th, tw)
# 0 - up; 1 - right; 2 - down; 3 - left
def RandNextCell(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return(x + dx, y + dy)
