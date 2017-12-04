import pandas as pd
import csv
import re
from collections import Counter

output = []
frequency = {}
colnames = ['username', 'firstname', 'surname', 'member_type', 'ts']
csv_columns = ['username','logins']


data = pd.read_csv("logins.csv", names=colnames)

'''
with open( 'logins.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
  '''


usernames = data.username.tolist()

print(usernames)

with open("usernames.txt", "w") as output:
    output.write(str(usernames))



##############COUNT###############

count = {}
dictionary = {}

for word in usernames :
    if word in count :
        count[word] += 1
    else:
        count[word] = 1




print(type(count))
print(count)


csv = open('count_list.csv', 'w')
columnTitleRow = "Username, Logins\n"
csv.write(columnTitleRow)

for (k,v) in Counter(count).iteritems():
    print "%s appears %d times" % (k, v)
    dictionary.update({k:v})




print(dictionary)

for key in dictionary.keys():
	username = key
	logins = dictionary[key]
	row = username + "," + str(logins) + "\n"
	csv.write(row)







