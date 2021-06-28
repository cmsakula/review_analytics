
data =[]
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip()) # strip remove white space and \n 
		#print(line)
print(len(data))
print(data[0])