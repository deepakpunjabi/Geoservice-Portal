'''

This program is to show  quality preferences when extra data
about the quality of neighbourhood is available

'''
from pyqtree import Index


class Dataset:
    def getType(self,type):
    	if(type == 0):
    		return 'feature'
    	elif(type == 1):
    		return 'star'
    	elif(type == 2):
    		return 'box'

    def __init__(self, id, x, y, type, quality):
        self.id = i
        self.bbox = (x, y, x, y)
        self.type = self.getType(type)
        self.quality = quality




index = Index(bbox=(0, 0, 80, 80))

p = [[0] * 2] * 2
q = []
k = 0

i1 = i2 = 0

# insert main data points
for i in range(20, 81, 40):
    for j in range(20, 81, 40):
        # p[i1][i2] = Dataset(k, i, j, 0)
        # q.append(p[i1][i2])
        temp = Dataset(k,i,j,0,0)
        q.append(temp)
        # print(str(i1)+'-'+str(i2)+' '+str(k)+' '+str(i)+' '+str(j))
        k += 1
        # index.insert(p[i1][i2], p[i1][i2].bbox)
        index.insert(temp, temp.bbox)
        i2 += 1
    i1 += 1
    i2 = 0

# for i in range(0,4):
# 	print(str(q[i].id)+' '+str(q[i].bbox[0])+' '+str(q[i].bbox[1]))

# set of star features
x = [] * 6
x.append(Dataset(4, 10, 70, 1,2))
x.append(Dataset(5, 30, 70, 1,5))
x.append(Dataset(10, 10, 30, 1,4))
x.append(Dataset(11, 30, 30, 1,8))
x.append(Dataset(12, 10, 10, 1,3))
x.append(Dataset(13, 50, 30, 1,6))

# insert  x points
for i in range(0, 6):
    index.insert(x[i], (x[i]).bbox)

# set of round features
y = [] * 6
y.append(Dataset(6, 10, 50, 2,3))
y.append(Dataset(7, 50, 70, 2,5))
y.append(Dataset(8, 70, 70, 2,1))
y.append(Dataset(9, 70, 50, 2,4))
y.append(Dataset(14, 70, 30, 2,2))
y.append(Dataset(15, 70, 10, 2,7))

# insert y points
for i in range(0, 6):
    index.insert(y[i], (y[i]).bbox)

# overlap regions
o9 = (0, 0, 80, 80)
o1 = (0, 20, 40, 60)
o2 = (40, 20, 80, 80)
o = (0, 0, 80, 80)

# matches = index.intersect(o)

# matches = sorted(matches, key=lambda x: x.id)

# scrap out type 0 points
#for i in range(0,3):
#	print('p('+i+')'+'\t')
neighbourhood_quality = []

for i in range(0,4):

	max_star = 0
	max_box = 0
	# print(str(i)+' '+str(q[i].id)+str(q[i].bbox[0]) + ',' + str(q[i].bbox[1]) + ')')
	print('feature'+str(i)+'  ('+str(q[i].bbox[0])+','+str(q[i].bbox[0])+') neighbours ---> ' )
	minx = q[i].bbox[0] - 20
	miny = q[i].bbox[1] - 20
	maxx = q[i].bbox[0] + 20
	maxy = q[i].bbox[1] + 20
	overlapbbox = (minx, miny, maxx, maxy)
	matches = index.intersect(overlapbbox)
	# find neighbours
	for match in matches:
		print(str(match.id)+' '+str(match.type))

	print("\nfiltering self....\n")
	# filter ownself
	for match in matches:
		if(match.id != i):
			print(str(match.id)+' '+str(match.type))
			if(match.type == 'star'):
				if(match.quality > max_star):
					max_star = match.quality
			else:
				if(match.quality > max_box):
					max_box = match.quality
	quality = max_box + max_star
	neighbourhood_quality.append((i,quality))

ranking = sorted(neighbourhood_quality, key=lambda x: x[1], reverse=True)

print('\nFinal ranking ...\n')
print('feature'+'\t'+'Rank')
for rank in ranking:
	print(str(rank[0])+'\t'+str(rank[1]))	


# for i in matches:
#     print('p' + str(i.id) + ' --> (' +
#           str(i.bbox[0]) + ',' + str(i.bbox[1]) + ')')
