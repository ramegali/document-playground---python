# Raphael Megali
# Program searches through file provided as an argument for strings (and comments)
# and outputs the results to a file.

from sys import argv, exit
import re, os.path

def main():
	if len(argv) <= 1:
		print "ERROR: You must provide a source file!"
		exit(1)

	if (os.path.isfile(argv[1])):
		fin = open(argv[1], 'r')
		outFile = argv[1].split(".")[0] + "Strings.txt"
		fout = open(outFile, 'w')
	else:	
		print "ERROR: Not a valid file!"
		exit(1)
	
	fout.write(fin.name + ":\n\n")
	lineNumber = 1
	for line in fin:
		matchComment = re.search(r"\s+//.+", line) # match anything starting with //
		matchString = re.search(r".*(\".+\")", line) # match anything in quotes

		# if you get both a comment and a string, output both on the same line
		if matchComment and matchString:                  
			bothMatched(matchComment, matchString, lineNumber, fout)
		# if you get just a comment
		elif matchComment:
			commentMatched(matchComment, lineNumber, fout)
		# if you get just a string
		elif matchString:
			stringMatched(matchString, lineNumber, fout)
		lineNumber += 1

	fin.close()
	fout.close()

def commentMatched(matchComment, lineNumber, fout):
	# strip leading whitespaces
	matchComment = str(lineNumber) + ": " + matchComment.group().strip() + "\n"
	fout.write(matchComment)

def stringMatched(matchString, lineNumber, fout):
	# split match into strings divided by quotation marks
	split = matchString.group().split("\"")
	line = str(lineNumber) + ": "
	for index in split:
		# find the string indexes with words in between quotes
		if re.match(r"\w+.?", index):
			line += index + "\t"
	line += "\n"
	fout.write(line)

def bothMatched(matchComment, matchString, lineNumber, fout):
	split = matchString.group().split("\"")
	for index in split:
		if re.match(r"\w+.?", index):
			matchString = str(lineNumber) + ": " + index
			fout.write(matchString)
	matchComment = "\t" + matchComment.group().strip() + "\n"
	fout.write(matchComment)

if __name__ == "__main__":
	main()
