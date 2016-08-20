PX = 200.0
PY = 200.0

PWIDTH = 100.0
PHEIGHT = 100.0

from math import sin, cos, atan, pi as PI
moi, goat = None, None

def setup():
    global moi, goat
    size(1000, 1000)
    background(0)
    smooth()
    stroke(0, 255, 255, 255)
    noFill()
    paddock()
    moi = Moi()
    goat = Goat(moi)

def paddock():
    stroke(0, 255, 255, 255)
    rect(PX, PY, PWIDTH, PHEIGHT)

class Goat:

    def __init__(self, target):
        self.x, self.y = PX + 1, PY + PHEIGHT -1
        self.target = target
        self.get_mad()
        self.target.panic()
        self.steps = 0

    def get_mad(self):
        self.chase()
        self.v = 0.5 * PI * self.target.v

    def next(self):
        self.dx = cos(self.angle) * self.v
        self.dy = sin(self.angle) * self.v
        self.x += self.dx
        self.y += self.dy
        self.draw()
        self.chase()
        self.steps += 1

    def chase(self):
        dy = self.target.y - self.y
        dx = self.target.x - self.x
        self.angle = atan2(dy, dx)

    def draw(self):
        stroke(255, 255, 0, 255)
        rect(self.x, self.y, 1, 1)    
        
    def got_em(self):
        return abs(self.x - self.target.x) < 1 and abs(self.y - self.target.y) < 1

class Moi:

    def __init__(self):
        self.x, self.y = PX + PWIDTH - 1, PY + PHEIGHT - 1
        self.v = 1.0
        self.steps = 0

    def panic(self):
        self.angle = 1.5 * PI

    def next(self):
        dx = cos(self.angle) * self.v
        dy = sin(self.angle) * self.v
        self.x += dx
        self.y += dy
        self.draw()
        self.steps += 1

    def draw(self):
        stroke(255, 0, 0, 255)
        rect(self.x, self.y, 1, 1)

    def escaped(self):
        return self.y < PY - 1


def draw():
    if not moi.escaped() and not goat.got_em():
        moi.next()

    if not goat.got_em():
        goat.next()

    if goat.got_em() or moi.escaped():
        print "Goat took %s steps" % goat.steps
        print "I took %s steps" % moi.steps
    
    