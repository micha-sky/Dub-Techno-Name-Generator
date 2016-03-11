import random
from random import randint

words = [line.rstrip('\n') for line in open('wordlist.txt')]

prefixIndex = 0
suffixIndex = 0
attachementIndex = 0
i = 0

for word in words:
	if word == "Prefixes:":
		prefixIndex = i
	elif word == "Suffixes:":
		suffixIndex = i
	elif word == "Attachement:":
		attachementIndex = i
	i = i + 1


prefixes = words[prefixIndex+1:suffixIndex-1]
suffixes = words[suffixIndex+1:attachementIndex-1]
attachements = words[attachementIndex+1:]


for x in range(0,9):
	prefix = random.choice(prefixes)
	suffix = random.choice(suffixes)
	attachement = random.choice(attachements)
	rand = randint(0,3)
	if rand <= 2:
		print prefix + suffix
	elif rand == 3:
		print prefix + suffix + " " + attachement
