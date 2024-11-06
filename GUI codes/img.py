from PIL import Image
from numpy import asarray
image = Image.open('im_300.jpg')
numpydata = asarray(image)
x = numpydata.reshape(-1)
print(x)