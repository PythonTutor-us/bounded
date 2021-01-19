
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
from collections import namedtuple


Color = namedtuple("Color","red,green,blue")
black = Color(0,0,0)


img = mpimg.imread("test.jpg")
cs = np.copy(img)
c = Color(200,200,200)

select = (img[:,:,0]<c.red)|(img[:,:,1]<c.green)|(img[:,:,2]<c.blue)

cs[select]=black
plt.imshow(cs)
plt.show()
