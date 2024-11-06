from PyQt5.QtGui import QImage, QPixmap
from PIL.ImageQt import ImageQt

# Load the image using Pillow
pil_image = Image.open('sh.jpg')

# Convert the Pillow image to a PyQt5 image
q_image = QImage(ImageQt(pil_image))

# Create a pixmap from the QImage
pixmap = QPixmap.fromImage(q_image)

# Set the pixmap on a QLabel
label.setPixmap(pixmap)
