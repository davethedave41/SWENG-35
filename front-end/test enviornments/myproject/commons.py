import torch
import torch.nn as nn
from torchvision import models
from PIL import Image
import torchvision.transforms as transforms

def get_model():
	model_path = "G_AB_0.pth"
	model = models.G_AB_0(pretrained=True)
	model.eval()
	return model

def get_tensor(image_bytes):
	my_transforms = transforms.Compose([transforms.Resize(256),
        				    transforms.CenterCrop(224),
        				    transforms.ToTensor(),
        				    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                             					  std=[0.229, 0.224, 0.225])])
	image = Image.open(io.BytesIO(image_bytes))
	return my_transforms(image).unsqueeze(0)

def predict_image(model, image_bytes):
	image_tensor = get_tensor(image_bytes)
	output = model(image_tensor)
	