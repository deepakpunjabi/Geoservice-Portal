from pyqtree import Index

class Dataset:
	def __init__(self,id,x,y):
		self.id = id
		self.bbox = (x,y,x,y)

index = Index(bbox=(0,0,100,100))

p1 = Dataset(1,25,25)
p2 = Dataset(2,25,75)
p3 = Dataset(3,75,75)
p4 = Dataset(4,75,25)

index.insert(p2,p2.bbox)
index.insert(p1,p1.bbox)
index.insert(p4,p4.bbox)
index.insert(p3,p3.bbox)

o1 = (0,0,100,100)

matches = index.intersect(o1)

for match in matches:
	print(match.id)