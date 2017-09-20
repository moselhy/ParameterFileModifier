import os, sys

def printUsage():
	print("%s DIRECTORY TAGNAME NEWVALUE" % sys.argv[0])


if len(sys.argv) < 4:
	print("Insufficient arguments. Usage: ")
	printUsage()
	sys.exit(1)

dirName = sys.argv[1]
tagToReplace = sys.argv[2]
newValue = ' '.join(sys.argv[3:])

if not os.path.exists(os.path.realpath(dirName)):
	print("Directory %s does not exist" % dirName)
	printUsage()
	sys.exit(1)

for file in os.listdir(dirName):
	file = os.path.join(dirName, file)
	fp = open(file, "r+")
	# Get a list of the lines that the file contains
	originalContent = fp.read().split('\n')
	newContent = []
	# Make a dictionary of the tags and their values
	tagDict = {}
	for line in originalContent:
		tokens = line.strip('()').split(' ')
		tagname = tokens[0]
		if tagname == tagToReplace:
			newContent.append('(%s %s)' % (tagname, newValue))
		else:
			newContent.append(line)

	fp.seek(0)
	fp.truncate()
	fp.write('\n'.join(newContent))
	fp.close()

print("Done processing %d files" % len(os.listdir(dirName)))