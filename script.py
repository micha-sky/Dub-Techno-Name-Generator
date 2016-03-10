import random
from random import randint

words = [line.rstrip('\n') for line in open('wordlist.txt')]

prefixIt = 0
suffixIt = 0
bothIt = 0
attachementIt = 0
i = 0

for word in words:
	if word == "Prefixes:":
		prefixIt = i
	elif word == "Suffixes:":
		suffixIt = i
	elif word == "Both:":
		bothIt = i
	elif word == "Attachement:":
		attachementIt = i
	i = i + 1


prefixes = words[prefixIt+1:suffixIt-1]
suffixes = words[suffixIt+1:bothIt-1]
both = words[bothIt+1:attachementIt-1]
attachements = words[attachementIt+1:]

prefix = random.choice(prefixes)
suffix = random.choice(suffixes)
bothWord = random.choice(both)
attachement = random.choice(attachements)


random = randint(0,5)

if random == 0:
	print prefix + " " + suffix
elif random == 1:
	print prefix + " " + suffix + " " + attachement
elif random == 2:
	print bothWord + " " + suffix
elif random == 3:
	print bothWord + " " + suffix + " " + attachement
elif random == 4:
	print prefix + " " + bothWord
elif random == 5:
	print prefix + " " + bothWord + " " + attachement 
