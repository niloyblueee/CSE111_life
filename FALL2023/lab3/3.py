import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z
        print(f'Vector <{self.x}, {self.y}, {self.z}> created.')

# Write your driver code here
v1=Vector3D(2,-3,1)
v2=Vector3D(-1,4,0)
mag1=math.sqrt(v1.x**2+v1.y**2+v1.z**2)
mag2=math.sqrt(v2.x**2+v2.y**2+v2.z**2)
dot=v1.x*v2.x+v1.y*v2.y+v1.z*v2.z
cross=v1.y*v2.z-v1.z*v2.y, v1.z*v2.x-v1.x*v2.z,v1.x*v2.y-v1.y*v2.x
print(f'Magnitude of the first vector = {mag1}')
print(f'Magnitude of the second vector = {mag2}')
print(f'Dot product of the two vectors = {dot}')
v3=Vector3D(cross[0],cross[1],cross[2])
print(f'Cross product of the two vectors = <{v3.x}, {v3.y}, {v3.z}>')
#https://docs.google.com/document/d/1jWyYz0JwV_PvVVpjSyKd0n_pMSlkOVmSFesMwzi2wGs/edit