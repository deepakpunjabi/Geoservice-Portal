from pyqtree import Index

class Dataset:
	def __init__(self,id,x,y):
		self.id = id
		self.bbox = (x,y,x,y)
		# self.bbox.minx=minx
		# self.bbox.miny=miny
		# self.bbox.maxx=maxx
		# self.bbox.maxy=maxy

spidex = Index(bbox=(0,0,100,100))

p1 = Dataset(1,20,80)
p2 = Dataset(2,80,80)
p3 = Dataset(3,40,60)
p4 = Dataset(4,60,60)
p5 = Dataset(5,80,60)
p6 = Dataset(6,40,30)
p7 = Dataset(7,60,30)
p8 = Dataset(8,80,30)
p9 = Dataset(9,60,20)
p10 = Dataset(10,60,90)

spidex.insert(p10,p10.bbox)

spidex.insert(p2, p2.bbox)
spidex.insert(p7, p7.bbox)
spidex.insert(p8, p8.bbox)
spidex.insert(p9, p9.bbox)
spidex.insert(p1, p1.bbox)
spidex.insert(p3, p3.bbox)
spidex.insert(p4, p4.bbox)
spidex.insert(p5, p5.bbox)
spidex.insert(p6, p6.bbox)


o1 = (0,0,100,100)
o2 = (25,25,75,75)
o3 = (0,0,75,75)
o4 = (25,25,75,75)
o5 = (25,25,100,100)
o6 = (25,25,50,50)
o7 = (25,50,100,100)
o8 = (50,50,100,100)

matches = spidex.intersect(o8)
#print(matches)
# res = sorted(matches)
# print(res)

for i in matches:
	print(i.id)
	# print(spidex.countmembers()+"\n")
