import math

class TopCan(object):
	
	pi = 2*math.acos(0)
	
	def __init__(self, vol):
		self.vol = vol
	
	def getRadiusHeight(self, vol, pi):
		dimensions = []
		print vol
		r = (vol / 4* pi) ** (1. / 3)
		print r
		dimensions.append(r)
		h = vol / (pi*(r**2))
		dimensions.append(h)
		return dimensions
	
	def minSurface(self, r, h, pi):
		self.a = 2*pi*r*(r+h)
		return self.a

		
v = int(raw_input("Enter volume> "))
can = TopCan(v)
#print can.pi
canDim = can.getRadiusHeight(v, can.pi)
print canDim
surfaceArea = can.minSurface(canDim[0], canDim[1], can.pi)
print surfaceArea