
data =[]
count = 0
message_length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip()) # strip remove white space and \n 
		message_length = len(data[count]) + message_length
		count += 1
		#if count % 1000 == 0:
		#	print(len(data))

print('there are ', len(data), 'messages. ', 'The average message length is ', message_length/len(data))
print('the message_length is ', message_length)

message_length = 0
for d in data:
	message_length = message_length + len(d)
print('the next message_length us ', message_length)