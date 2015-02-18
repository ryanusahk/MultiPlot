from sys import argv
import sys
import glob
import os
import json

# class media:
# 	def __init__(self, name):
# 		self.name = name
# 		self.replicates = []
# 		self.blank = []

# 	def numReplicates():
# 		return len(self.replicates)

# class data:
# 	def __init__(self, name, datapoints):
# 		self.wellName = name
# 		self.datapoints = datapoints

def coordToIndex(coord):
	coord = coord.upper()
	key = 'ABCDEFGH'
	row = key.index(coord[0])
	column = int(coord[1:]) - 1
	return (row * 12) + column

def getData(coord):
	index = coordToIndex(coord)
	return sortedData[index]

tempFile = open(argv[1]).read().split('\n')
format = open('format.txt').read().split('----------------------------\n')
format = format[2:]

plateCheck = 'ABCDEFGH'
file = []

for line in tempFile:
    if len(line)>5 and line[0] in plateCheck:
        file.append(line)

timepoints = []
plate = []
sortedData = []

count = 1
for line in file:
	plate.append(line.split("	")[1:-1])
	if (count == 8):
		timepoints.append(plate)
		count = 0
		plate = []
	count += 1

for y in range(8):
	for x in range(12):
		wellData = []
		for point in timepoints:
			wellData.append(float(point[y][x]))
		sortedData.append(wellData)

numPoints = len(timepoints)

dictionary = {}

# def convert_to_builtin_type(obj):
#     print 'default(', repr(obj), ')'
#     # Convert objects to a dictionary of their representation
#     d = { '__class__':obj.__class__.__name__, 
#           '__module__':obj.__module__,
#           }
#     d.update(obj.__dict__)
#     return d

for graphFormat in format:
	info = graphFormat.split('\n')
	name = info[1]
	mediaName = info[2]
	replicates = info[3].split(' ')
	blank = info[4]

	if name == '':
		# print('Done!')
		newFile = open(argv[1] + "_DATA.txt", "w")
		newFile.write(json.dumps(dictionary))
		newFile.close()
		print "Done!"
		sys.exit()
	else:

		listOfSets = []

		for reps in replicates:
			listOfSets.append(getData(reps))
		
		listOfSets.append(getData(blank))
		
		dictionary[name + ' ' + mediaName] = listOfSets



		# path = glob.glob(os.path.dirname(os.path.abspath(__file__)))[0]


