# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:13:40 2020

@author: malrawi
"""

import torchvision.transforms as transforms
from datasets import ImageDataset
import torch
from pix2pix_models import GeneratorUNet
from matplotlib import pyplot as plt
import matplotlib as mpl
from PIL import Image
from mod_nipy_spectral import cmap
import scipy.io
import numpy as np
import matplotlib.patches as mpatches
import io

mat = scipy.io.loadmat('label_list.mat')
label_list = []
for l in range(59):
    label_list.append(str(mat['label_list'][0][l][0]))


# A is the fashion image
# B is the pixel-level annotation

model_name = 'generator_800.pth' 
dataset_name = 'ClothCoParse'
experiment_name = '' # to be added 
path2model = './saved_models/'
output_channels = 1

print('model used', model_name) 

# loads a saved model
def get_GAN_AB_model(folder_model, model_name, device):          
    G_AB = GeneratorUNet(out_channels=output_channels)   
    G_AB.load_state_dict(torch.load(folder_model + model_name,  map_location=device ),  )    
    G_AB.eval()            
    return G_AB


in_shape = (512, 512)
transforms_used = transforms.Compose( 
    [ transforms.Resize(in_shape, Image.BICUBIC),
     transforms.ToTensor(), 
     transforms.Normalize((0.5,0.5,0.5), (.5,.5,.5)) 
                 ] ) 

data_set = ImageDataset("../data/%s" % dataset_name, 
                     transforms_A=None, 
                     transforms_B=None, 
                     mode="train", 
                     unaligned=False, 
                     HPC_run=0, 
                     Convert_B2_mask = 0,
                     channels= output_channels
                 )

cuda = False # this will definetly work on the cpu if it is false
if cuda:
    cuda = True if torch.cuda.is_available() else False
device = torch.device('cuda' if cuda else 'cpu')

G_AB = get_GAN_AB_model(path2model, model_name,  device) # load the model


img_id=torch.randint( len(data_set), (1,)) # getting some image, here index 100
PIL_A_img = data_set[img_id]['A']
PIL_B_img = data_set[img_id]['B']
real_A = transforms_used(PIL_A_img)  # tensor image
    
    
if cuda: real_A = real_A.to(device)
with torch.no_grad():
    B_output = G_AB(real_A.unsqueeze(0))
    
#PIL_A_img.show() # show the original image

def show_tensor(img, show_img=True):
    to_pil = transforms.ToPILImage()
    img = to_pil(img.squeeze())  # we can also use test_set[1121][0].numpy()
    if show_img:
        arr = np.unique(np.asarray(img))
        print(arr)

        im = plt.imshow(img.convert('L'))  # show the pixel-level annotation
        plt.show()

        im = plt.imshow(img.convert('L'),  cmap= cmap, vmin=0, vmax=arr[len(arr)-1]) # show the pixel-level annotation
        plt.show()

        plt.axis('off')
        #plt.show(); #shows the plotted image

        '''
        mat = scipy.io.loadmat('label_list.mat')
        labels = []
        for l in range(len(arr)):
            labels.append(str(mat['label_list'][0][arr[l]][0]))

        labels[0] = "background"

        colors = [ im.cmap(im.norm(value)) for value in arr]
        patches = [ mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(arr))]
        plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
        '''


        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        #img = Image.open(buf)
        #img.show()
        #buf.close()
        # img.show()
        # img.save('/home/malrawi/GAN_seg_img_414/'+'gg-col'+'.png') # can be used to save the image

    return img

im = show_tensor(B_output)

