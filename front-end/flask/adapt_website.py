from flask import Flask, redirect, url_for, render_template

# instance of a flask web application
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/aboutus")
def AboutUs():
	return render_template("aboutus.html")

@app.route('/uploadimage')
def UploadImage():
	return render_template("uploadimage.html")

@app.route('/tcdadapt')
def TCDAdapt():
	return render_template("tcdadapt.html")

if __name__ == "__main__":
    app.run(debug=True)