'''

This program is to show  quality preferences when extra data
about the quality of neighbourhood is available

'''
from pyqtree import Index

class Dataset:
	def __init__(self,id,x,y,type):
		self.id = id
		self.bbox = (x,y,x,y)
		self.type = type

index = Index(bbox=(0,0,80,80))

p = [[0]*4]*4
k = 0

i1 = i2 = 0

# insert main data points
for i in range(20,81,40):
	for j in range(20,81,40):
		p[i1][i2] = Dataset(k,i,j,0)
		k += 1
		index.insert(p[i1][i2],(p[i1][i2]).bbox)
		i2 +=1
	i1+=1
	i2 = 0

# set of star features
x = []*6
x[1] = Dataset(4,10,70,1)
x[2] = Dataset(5,30,70,1)
x[3] = Dataset(10,10,30,1)
x[4] = Dataset(11,30,30,1)
x[5] = Dataset(12,10,10,1)
x[6] = Dataset(13,50,30,1)


# insert  x points
for i in range(1,7):
	index.insert(x[i],(x[i]).bbox)

# set of round features
y = []*6
y[1] = Dataset(6,10,50,2)
y[2] = Dataset(7,50,70,2)
y[3] = Dataset(8,70,70,2)
y[4] = Dataset(9,70,50,2)
y[5] = Dataset(14,70,30,2)
y[6] = Dataset(15,70,10,2)

# insert y points
for i in range(1,7):
	index.insert(y[i],(y[i]).bbox)

# overlap regions
o9 = (0,0,80,80)
o1 = (0,20,40,60)
o2 = (40,20,80,80)
o = (0,0,80,80)

matches = spidex.intersect(o)
matches = sorted(matches, key=lambda x:x.id)

for i in matches:
	# print(str(i.id))
	print('p'+str(i.id)+' --> ('+str(i.bbox[0])+','+str(i.bbox[1])+')')
