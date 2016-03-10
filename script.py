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
suffixes = words[suffixIt+1:attachementIt-1]
attachements = words[attachementIt+1:]

prefix = random.choice(prefixes)
suffix = random.choice(suffixes)
attachement = random.choice(attachements)


random = randint(0,1)

if random == 0:
	print prefix + suffix
elif random == 1:
	print prefix + suffix + " " + attachement
