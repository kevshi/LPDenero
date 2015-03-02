import sqlite3
import glob

filenames = glob.glob('./videofiles/*.txt')
namewithtext = []

for file in filenames:
	textread = open(file, "r")
	text = ''
	for line in textread:
		line = line.replace('\n', '')
		text += ' ' + line;
	namewithtext.append((file, text))

with sqlite3.connect("videotext.db") as connection:
	c = connection.cursor()
	c.execute("""DROP TABLE videos""")	
	c.execute("""CREATE TABLE videos(title TEXT, description TEXT)""")
	c.executemany("INSERT INTO videos (title, description) VALUES (?, ?)", namewithtext)
