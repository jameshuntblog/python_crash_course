import numpy as np
from PIL import Image

im = Image.open('C:\\Users\\James Hunt\\Documents\\GitHub\\python_learning\\'\
    'python_crash_course_2e\\alien_invasion\\images\\ship.bmp')
data = np.array(im)

r1, g1, b1 = 230, 230, 230 # Original value
r2, g2, b2 = 0, 0, 0 # Value that we want to replace it with

red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
mask = (red == r1) & (green == g1) & (blue == b1)
data[:,:,:3][mask] = [r2, g2, b2]

im = Image.fromarray(data)
im.save('C:\\Users\\James Hunt\\Documents\\GitHub\\python_learning\\'\
    'python_crash_course_2e\\alien_invasion\\images\\ship_modified.bmp')