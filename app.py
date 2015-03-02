from flask import Flask, render_template, redirect, url_for, request, \
				  session, flash, g
import sqlite3
from searchalgorithm import search, searchAllFiles

app = Flask(__name__)
app.database = "videotext.db"
query = ''

#homepage
@app.route('/', methods = ['GET', 'POST'])
def home():
	error = None
	if request.method == 'POST':
		global query 
		query = request.form['search']
		if request.form['search'] == '':
			error = 'Did not input search, please re-enter.'
		else:
			return redirect(url_for('result'))
	return render_template('index.html', error=error)


#results page
@app.route('/result')
def result():
	#database, initializes video
	g.db = connect_db()
	cur = g.db.execute('select * from videos')
	videos = [[row[0], row[1]] for row in cur.fetchall()]
	count = 0
	for video in videos:
		k = search(video[0], query)
		video[1] = k
		video[0] = video[0].replace('./videofiles/', '')
		video[0] = video[0].replace('.txt', '')
	for video in videos:
		count += video[1]

	return render_template('result.html', title = video[0], description = video[1])

#creates database object
def connect_db():
	return sqlite3.connect(app.database)

# runs application
app.debug = True
if __name__ == '__main__':
    app.run()