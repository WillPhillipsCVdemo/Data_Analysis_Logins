import pandas as pd
import csv
import re
from collections import Counter

output = []
frequency = {}
colnames = ['username', 'firstname', 'surname', 'member_type', 'ts']
csv_columns = ['username','logins']


data = pd.read_csv("logins.csv", names=colnames)

data2 = pd.read_csv("logins.csv", names=colnames)

'''
with open( 'logins.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
  '''

##Single File
#usernames = data.username.tolist()


##Concatenate

concat = pd.concat([data,data2])
usernames2 = concat.username.tolist()

print(usernames2)

with open("usernames2.txt", "w") as output:
    output.write(str(usernames2))



##############COUNT###############

count = {}
dictionary = {}

for word in usernames2 :
    if word in count :
        count[word] += 1
    else:
        count[word] = 1




print(type(count))
print(count)


csv = open('count_list2.csv', 'w')
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







