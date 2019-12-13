"""
<x=16, y=-8, z=13>
<x=4, y=10, z=10>
<x=17, y=-5, z=6>
<x=13, y=-3, z=0>
"""


class Moon:
    def __init__(self, x, y, z):
        self.pos = (x,y,z)
        self.vel = (0,0,0)
        self.positions = set()

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
        self.positions.add(self.pos)

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

m1 = Moon(-8,  -10, 0   )
m2 = Moon( 5, 5   , 10   )
m3 = Moon( 2, -7  ,  3   )
m4 = Moon( 9,  -8 ,   -3 )
moonList = [m1, m2, m3, m4]

def move_moons(moonList):
    for moon in moonList:
        for other in moonList:
            if moon != other:
                moon.apply_gravity(other)
    for moon in moonList:
        moon.move()

    for moon in moonList:
        print(moon)

for moon in moonList:
    print(moon)

for i in range(100):
    print("========================================")
    move_moons(moonList)

energy = sum([m.total_energy() for m in moonList])

print([len(m.positions) for m in moonList])
print(energy)
