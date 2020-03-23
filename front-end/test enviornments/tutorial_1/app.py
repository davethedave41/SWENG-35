from flask import Flask, jsonify, request
import io
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import json

app = Flask(__name__)
imagenet_class_index = json.load(open("imagenet_class_index.json"))

# pass 'pretrained' as 'True' to use the pretrained weights
model = models.densenet121(pretrained=True)
# since we are using our model only for inference, switch to 'eval' mode
model.eval()

# transform image method used to take image data in bytes and apply series of transforms
# and returns tensor

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

# method uses pretrained densenet model to get actual predicition from model

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]


# Test for get_prediction
#
#with open("cat.jpeg", 'rb') as f:
#    image_bytes = f.read()
#    print(get_prediction(image_bytes=image_bytes))


# Test for transform_image method
#
#with open("cat.jpeg", 'rb') as f:
#    image_bytes = f.read()
#    tensor = transform_image(image_bytes=image_bytes)
#    print(tensor)





@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # get file from request
        file = request.files['file']
        # convert file to bytes
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        return jsonfiy({'class_id': 'IMAGE_NET_XXX', 'class_name': 'Cat'})


if __name__ = '__main__':
    app.run()