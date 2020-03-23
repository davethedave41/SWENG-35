from flask import Flask, request, render_template

app = Flask(__name__)

## import functions from classes
from commons import get_tensor
from inference import get_response_image



@app.route('/predict', methods=['GET', 'POST'])
def predict():

 if flask.request.method == 'GET':
  return render_template('index.html', value='hi')

  # user has uploaded image
 if flask.request.method == 'POST':
 	if flask.request.files.get("image"):
 		# read uploaded image
 		image = flask.request.files["image"].read()
 		image = Image.open(io.BytesIO("image"))

 		# send image to model and get output
 		output_image = get_response_image(image_bytes=image)
 		return render_template('result.html', output_image)


# flask will restart whenever changes are saved
if __name__ == '__main__':
    app.run(debug=True)
