"""
<x=16, y=-8, z=13>
<x=4, y=10, z=10>
<x=17, y=-5, z=6>
<x=13, y=-3, z=0>
"""

import math


def compute_lcm(x,y):
    return x*y//math.gcd(x,y)

class Moon:
    def __init__(self, x, y, z):
        self.pos = (x,y,z)
        self.vel = (0,0,0)

    def apply_gravity(self, other):
        x,y,z = self.pos
        x1,y1,z1 = other.pos
        dx = self.normalize(x1-x) 
        dy = self.normalize(y1-y) 
        dz = self.normalize(z1-z) 

        vx,vy,vz = self.vel
        self.vel = (vx+dx, vy+dy, vz+dz)

    @staticmethod
    def normalize(value):
        if value == 0:
            return value
        if value > 0:
            return 1
        return -1

    def move(self):
        x,y,z = self.pos
        vx,vy,vz = self.vel
        self.pos = (x+vx, y + vy, z + vz)
        x,y,z = self.pos



    def __repr__(self):
        x,y,z = self.pos
        vx,vy,vz = self.vel
        return f"<{x} {y} {z}>  <{vx}, {vy}, {vz}>"

    def potential_energy(self):
        return sum([abs(a) for a in self.pos])
    
    def kinetic_energy(self):
        return sum([abs(a) for a in self.vel])
    
    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()


m1 = Moon(16, -8, 13)
m2 = Moon(4,  10, 10)
m3 = Moon(17, -5, 6)
m4 = Moon(13, -3, 0)
"""
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""

#m1 = Moon(-1,  0, 2   )
#m2 = Moon( 2, -10   , -7   )
#m3 = Moon( 4, -8 ,  8   )
#m4 = Moon( 3,  5 ,   -1 )
moonList = [m1, m2, m3, m4]

def move_moons(moonList):
    for moon in moonList:
        for other in moonList:
            if moon != other:
                moon.apply_gravity(other)
    for moon in moonList:
        moon.move()

xs = tuple([m.pos[0] for m in moonList]+[m.vel[0] for m in moonList])
ys = tuple([m.pos[1] for m in moonList]+[m.vel[1] for m in moonList])
zs = tuple([m.pos[2] for m in moonList]+[m.vel[2] for m in moonList])
xstates = set([xs])
ystates = set([ys])
zstates = set([zs])

i = 0
printedx = False
printedy = False
printedz = False
results = []
while True:
    move_moons(moonList)
    i = i+1
    for moon in moonList:
        xs = tuple([m.pos[0] for m in moonList]+[m.vel[0] for m in moonList])
        ys = tuple([m.pos[1] for m in moonList]+[m.vel[1] for m in moonList])
        zs = tuple([m.pos[2] for m in moonList]+[m.vel[2] for m in moonList])
        if xs in xstates and not printedx:
            print(i)
            results.append(i)
            printedx = True
        if ys in ystates and not printedy:
            printedy = True
            results.append(i)
            print(i)
        if zs in zstates and not printedz:
            printedz = True
            results.append(i)
            print(i)
    
    if  all((printedx, printedy, printedz)):
        break

r1, r2, r3 = tuple(sorted(results, reverse = True))
r_final = compute_lcm(compute_lcm(r1,r2),r3)
print(r_final)

