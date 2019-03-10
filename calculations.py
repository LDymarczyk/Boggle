cubes = """Z,M,Ć,T,U,J
A,E,I,U,Y,O
E,W,Ś,I,S,L
F,Ę,S,J,H,L
Ą,G,T,C,Ń,M
O,Ż,W,S,T,C
P,Ł,I,K,R,O
N,N,A,C,P,I
A,O,Z,Y,E,Z
A,A,I,M,Y,K
E,Ź,B,Z,E,P
E,A,A,Ł,D,Y
Ó,D,Z,N,W,H
S,R,G,O,L,A
I,I,W,R,N,B
N,O,R,K,D,E"""

cubes = cubes.split("\n")
unique = set()
for cube in cubes:
    cubes[cubes.index(cube)] = cube.split(',')
    unique |= ({*cube})

import pdb; pdb.set_trace()