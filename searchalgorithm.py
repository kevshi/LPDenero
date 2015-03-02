import glob

filenames = glob.glob('./videofiles/*.txt')

def searchAllFiles(fileList, query):
	count = 0
	for file in fileList:
		count += search(file, query)
	return count

def search(textfile, query):
	searchfile = open(textfile, "r")
	count = 0
	for line in searchfile:
	    if query in line:
	    	count += 1
	searchfile.close()
	return count