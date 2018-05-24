#encoding=utf-8

import math

math.acos()


print('hello world!')
print('12*10={}'.format(12*10))

print('25的开方等于: {}'.format(math.sqrt(25)))


from PIL import Image
img = Image.open('image.jpg')
print(img.size)


import numpy as np
img_array = np.array(img)
img_array.shape


img.save('aaa.jpg')