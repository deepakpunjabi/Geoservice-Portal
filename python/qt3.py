from pyqtree import Index

class Dataset:
	def __init__(self,id,x,y):
		self.id = id
		self.bbox = (x,y,x,y)

spidex = Index(bbox=(0,0,80,80))

p = [[0]*4]*4
k = 0

i1 = i2 = 0
for i in range(10,81,20):
	for j in range(10,81,20):
		p[i1][i2] = Dataset(k,i,j)
		k += 1
		spidex.insert(p[i1][i2],(p[i1][i2]).bbox)
		i2 +=1
	i1+=1
	i2 = 0

o9 = (0,0,80,80)
o1 = (0,20,40,60)
o2 = (40,20,80,80)

matches = spidex.intersect(o2)
# matches = sorted(matches, key=lambda x:x.id)
for i in matches:
	# print(str(i.id))
	print('p'+str(i.id)+' --> ('+str(i.bbox[0])+','+str(i.bbox[1])+')')
