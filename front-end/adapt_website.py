

from flask import Flask, redirect, url_for, render_template,request
from flask_sqlalchemy import SQLAlchemy


# instance of a flask web application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
db = SQLAlchemy(app)

num=0

class photos(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	originalPhoto = db.Column(db.Text, nullable=False)
	target = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return 'Photo '+ str(self.id)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/aboutus")
def AboutUs():
	return render_template("aboutus.html")

@app.route('/uploadimage', methods=['GET', 'POST'])
def UploadImage():

	if request.method == 'POST':
		all_photos = photos.query.all()[int(request.form['title'])]
		return render_template("uploadimage.html",photos=all_photos)
		
	
	with open("original.txt") as f:
		cnt = 1
		for s_line in f:
			photo_title = str(cnt)
			photo_originalPhoto = s_line
			photo_target =""
			new_photo = photos(
            title=photo_title, originalPhoto=photo_originalPhoto, target=photo_target)
			db.session.add(new_photo)
			db.session.commit()
			cnt +=1

	with open("target.txt") as f:
		cnt2 =0
		for s_line in f:
			photo = photos.query.all()[cnt2]
			photo.target = s_line
			db.session.commit()
			cnt2 +=1

	all_photos = photos.query.all()[0]
	return render_template("uploadimage.html", photos=all_photos)	

	

@app.route('/tcdadapt')
def TCDAdapt():
	return render_template("tcdadapt.html")

if __name__ == "__main__":
    app.run(debug=True)