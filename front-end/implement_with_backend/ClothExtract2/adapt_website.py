

# from flask import Flask, redirect, url_for, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# import load_then_test_model

# import glob
# from PIL import Image, ImageFilter

# import os

# import torchvision.transforms as transforms
# from datasets import ImageDataset
# from torch.utils.data import DataLoader
# import torch
# from matplotlib import pyplot as plt
# from models import GeneratorResNet



# # instance of a flask web application
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
# db = SQLAlchemy(app)


# APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# # path2model = '/Users/suzukimiyuki/Desktop/sweng2/github/SWENG-35/front-end/data/saved_models/monet2photo/'
# # model_name = 'G_AB_0.pth'
# # dataset_name = 'ClothCoParse' 
# using_test_data = True
# batch_test_size = 1 
# channels = 3 

# model_name = 'G_AB_0.pth' 
# dataset_name = 'ClothCoParse'
# experiment_name = '' # to be added 
# path2model = './saved_models/ClothCoParse/'

# # n_cpu = 0
# # input_shape = (channels, 0) # added 0 to resolve a problem

# # print('model used', model_name)


# # transforms_val = transforms.Compose( [ transforms.ToTensor(), 
# #                   transforms.Normalize((0.5,0.5,0.5), (.5,.5,.5)) 
# #                  ] ) 

# # data_set = ImageDataset("../data/%s" % dataset_name, 
# #                             transforms_ = None, 
# #                             unaligned=False, 
# #                             mode='train' )

# class photos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     originalPhoto = db.Column(db.Text, nullable=False)
#     target = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return 'Photo ' + str(self.id)



# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/aboutus")
# def AboutUs():
#     return render_template("aboutus.html")


# @app.route('/uploadimage', methods=['GET', 'POST'])
# def UploadImage():

# 	if request.method == 'POST':
# 		all_photos = photos.query.all()[2]
# 		target = os.path.join(APP_ROOT, 'static/')
# 		print(target)
# 		if not os.path.isdir(target):
# 			os.mkdir(target)
		
# 		for file in request.files.getlist("file"):
# 			print(file)
# 			filename = file.filename
# 			destination = "/".join([target, filename])
# 			print(destination)
# 			file.save(destination)
# 			real_A = load_then_test_model.transforms_used(Image.open(".../SWENG-35/front-end/implement_with_backend/ClothExtract2/static/"+filename).convert('RGB'))   # tensor image #change data path ".../SWENG-35/front-end/implement_with_backend/ClothExtract/static/"

# 		cuda = False # this will definetly work on the cpu if it is false
# 		if cuda:
# 			cuda = True if torch.cuda.is_available() else False
# 		device = torch.device('cuda' if cuda else 'cpu')
# 		G_AB = load_then_test_model.get_GAN_AB_model(path2model, model_name,  device) # load the model
# 		G_AB.eval()
# 		# if not cuda:
# 		#     G_AB=G_AB.cpu()
# 		if cuda: real_A = real_A.to(device)
# 		with torch.no_grad():
# 			B_output = G_AB(real_A.unsqueeze(0))
# 		#PIL_A_img.show() # show the original image            
# 		#plt.imshow(PIL_B_img.convert('L'),  cmap= plt.cm.get_cmap("nipy_spectral"), vmin=0, vmax=255) # show the pixel-level annotation
# 		#all_photos.target = (load_then_test_model.show_tensor(B_output)).save("/Users/suzukimiyuki/Desktop/mywork/ClothExtract/static/temp2.jpg", quality=95) # show the segmented image we get from the model   
# 		#(load_then_test_model.show_tensor(B_output)).save("/Users/suzukimiyuki/Desktop/mywork/ClothExtract/static/temp2.jpg", quality=95) # show the segmented image we get from the model   
# 		segmented_image = load_then_test_model.show_tensor(B_output)
# 		destination2 = "/".join([target, "2"+filename])
# 		segmented_image.save(destination2)  
# 		return render_template("uploadimage.html", image_A=filename, image_B="2"+filename )	

# 	with open("original.txt") as f:
# 		cnt = 1
# 		for s_line in f:
# 			photo_title = str(cnt)
# 			photo_originalPhoto = s_line
# 			photo_target = ""
# 			#new_photo = photos(title=photo_title, originalPhoto=photo_originalPhoto,target=photo_target)
# 			db.session.add(photos(title=photo_title, originalPhoto=photo_originalPhoto,target=photo_target))
# 			db.session.commit()
# 			cnt += 1
# 	with open ("target.txt") as f:
# 		cnt2 = 0
# 		for s_line in f:
# 			photo = photos.query.all()[cnt2]
# 			photo.target = s_line
# 			db.session.commit()
# 			cnt2 += 1
# 	all_photos = photos.query.all()[0]		
# 	return render_template("uploadimage.html", photos=all_photos)


    


# @app.route('/tcdadapt')
# def TCDAdapt():
#     return render_template("tcdadapt.html")


# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
#import load_then_test_model
import load_test_pix2pix

import glob
from PIL import Image, ImageFilter

import os

import torchvision.transforms as transforms
from datasets import ImageDataset,to_rgb
from torch.utils.data import DataLoader
import torch
from matplotlib import pyplot as plt
from models import GeneratorResNet



# instance of a flask web application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
db = SQLAlchemy(app)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# path2model = '/Users/suzukimiyuki/Desktop/sweng2/github/SWENG-35/front-end/data/saved_models/monet2photo/'
# model_name = 'G_AB_0.pth'
# dataset_name = 'ClothCoParse' 
using_test_data = True
batch_test_size = 1 
channels = 3 

#model_name = 'G_AB_0.pth' 
model_name = 'generator_800.pth'
dataset_name = 'ClothCoParse'
experiment_name = '' # to be added 
path2model = './saved_models/ClothCoParse/'

# n_cpu = 0
# input_shape = (channels, 0) # added 0 to resolve a problem

# print('model used', model_name)


# transforms_val = transforms.Compose( [ transforms.ToTensor(), 
#                   transforms.Normalize((0.5,0.5,0.5), (.5,.5,.5)) 
#                  ] ) 

# data_set = ImageDataset("../data/%s" % dataset_name, 
#                             transforms_ = None, 
#                             unaligned=False, 
#                             mode='train' )

class photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    originalPhoto = db.Column(db.Text, nullable=False)
    target = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'Photo ' + str(self.id)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/aboutus")
def AboutUs():
    return render_template("aboutus.html")


@app.route('/uploadimage', methods=['GET', 'POST'])
def UploadImage():

	if request.method == 'POST':
		all_photos = photos.query.all()[2]
		target = os.path.join(APP_ROOT, 'static')
		print(target)
		if not os.path.isdir(target):
			os.mkdir(target)
		
		for file in request.files.getlist("file"):
			print(file)
			filename = file.filename
			destination = "/".join([target, filename])
			print(destination)
			file.save(destination)
			# image_tmp = load_test_pix2pix.transforms_used(Image.open("/Users/suzukimiyuki/Desktop/example3/SWENG-35/front-end/implement_with_backend/ClothExtract2/static/"+filename))   # tensor image #change data path ".../SWENG-35/front-end/implement_with_backend/ClothExtract/static/"	
			# if image_tmp.mode != "RGB":		
			# 	image_tmp = to_rgb(image_tmp)
			# real_A = self.transform_A(image_tmp) # here we apply the transform on the source	
			real_A = load_test_pix2pix.transforms_used(Image.open("/Users/suzukimiyuki/Desktop/example6/SWENG-35/front-end/implement_with_backend/ClothExtract2/static/"+filename).convert("RGB"))   # tensor image #change data path ".../SWENG-35/front-end/implement_with_backend/ClothExtract/static/"
			# print("real_A.size:")
			# print(real_A.size)
			#real_A = to_rgb(real_A)

		#PIL_B_img = load_test_pix2pix.data_set[11]['B']
		cuda = False # this will definetly work on the cpu if it is false
		if cuda:
			cuda = True if torch.cuda.is_available() else False
		device = torch.device('cuda' if cuda else 'cpu')
		print("real_A:\n %s", real_A)
		G_AB = load_test_pix2pix.get_GAN_AB_model(path2model, model_name,  device) # load the model
		G_AB.eval()
		# if not cuda:
		#     G_AB=G_AB.cpu()
		if cuda: real_A = real_A.to(device)
		with torch.no_grad():
			B_output = G_AB(real_A.unsqueeze(0))
		#PIL_A_img.show() # show the original image            
		#plt.imshow(PIL_B_img.convert('L'),  cmap= plt.cm.get_cmap("nipy_spectral"), vmin=0, vmax=255) # show the pixel-level annotation
		#all_photos.target = (load_then_test_model.show_tensor(B_output)).save("/Users/suzukimiyuki/Desktop/mywork/ClothExtract/static/temp2.jpg", quality=95) # show the segmented image we get from the model   
		#(load_then_test_model.show_tensor(B_output)).save("/Users/suzukimiyuki/Desktop/mywork/ClothExtract/static/temp2.jpg", quality=95) # show the segmented image we get from the model   
		segmented_image = load_test_pix2pix.show_tensor(B_output)
		segmented_image = segmented_image.convert('RGB')
		#segmented_image2 = plt.imshow(segmented_image.convert('L'),  cmap= plt.cm.get_cmap("nipy_spectral"), vmin=0, vmax=60) # since we have 59 classes + background 
		destination2 = "/".join([target, "2"+filename])
		segmented_image.save(destination2)  
		#plt.imsave(destination2, segmented_image.convert('L'), cmap=plt.cm.get_cmap("nipy_spectral"))
		return render_template("uploadimage.html", image_A=filename, image_B="2"+filename )	

	with open("original.txt") as f:
		cnt = 1
		for s_line in f:
			photo_title = str(cnt)
			photo_originalPhoto = s_line
			photo_target = ""
			#new_photo = photos(title=photo_title, originalPhoto=photo_originalPhoto,target=photo_target)
			db.session.add(photos(title=photo_title, originalPhoto=photo_originalPhoto,target=photo_target))
			db.session.commit()
			cnt += 1
	with open ("target.txt") as f:
		cnt2 = 0
		for s_line in f:
			photo = photos.query.all()[cnt2]
			photo.target = s_line
			db.session.commit()
			cnt2 += 1
	all_photos = photos.query.all()[0]		
	return render_template("uploadimage.html", photos=all_photos)


    


@app.route('/tcdadapt')
def TCDAdapt():
    return render_template("tcdadapt.html")


if __name__ == "__main__":
    app.run(debug=True)

