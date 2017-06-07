# Raphael Megali
# Script searches for words in a text file
# and outputs total word count along with 
# 10 most common words and their counts to a file

from collections import Counter
from sys import argv, exit
import re, os.path

if len(argv) < 1:
	print "ERROR: Must provide source file!"
	exit(1)

if (os.path.isfile(argv[1])):
	fin = open(argv[1], 'r')
	outFile = argv[1].split(".")[0] + "WordCount.txt"
	fout = open(outFile, 'w')
else:
	print "ERROR: Not a valid file!"
	exit(1)

# find all the words
words = re.findall(r'\w+', fin.read().lower())

numWords = "Number of words: " + str(len(words))
fout.write(numWords)
fout.write("\n\nThe 10 most common words in the file are:\n")
count = Counter(words).most_common(10)
for key, value in count:
	fout.write(key)
	fout.write("\t")
	fout.write(str(value))
	fout.write("\n")

fin.close()
fout.close()