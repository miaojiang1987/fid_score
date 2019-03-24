import os 
import numpy as np
from PIL import Image
import sys

names=os.listdir('test_celeba')

for name in names:
    im=Image.open('test_celeba/'+name)
    im2arr=np.array(im,dtype=np.float32)
    im = Image.fromarray(im2arr.astype('uint8'))
    im2 = im.resize((32, 32), Image.NEAREST) 
    im2.save('celeba_resize/'+name+'.png')
