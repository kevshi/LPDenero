from flask import Flask, render_template, redirect, url_for, request, \
				  session, flash, g
import sqlite3
from searchalgorithm import search, searchAllFiles

app = Flask(__name__)
app.database = "videotext.db"

#homepage
@app.route('/', methods = ['GET', 'POST'])
def home():

	#database, initializes video
	g.db = connect_db()
	cur = g.db.execute('select * from videos')
	videos = [[row[0], row[1]] for row in cur.fetchall()]
	query = request.form['search']
	for video in videos:
		k = search(video[0], query)
		video[1] = k
		video[0] = video[0].replace('./videofiles/', '')
		video[0] = video[0].replace('.txt', '')

	error = None
	if request.method == 'POST':
		if query == '':
			error = 'Did not input search, please re-enter.'
		else:
			return redirect(url_for('result'))
	return render_template('index.html', error = error)


#results page
@app.route('/result')
def result():
	return render_template('result.html', videos = videos)

#creates database object
def connect_db():
	return sqlite3.connect(app.database)

#runs application
# if __name__ == '__main__':
#     app.run()