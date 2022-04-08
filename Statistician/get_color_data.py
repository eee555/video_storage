from PIL import Image  
import numpy as np  

i = Image.open('./color.png') 
i = np.array(i)[0, :, :3]
i = i[np.round(np.linspace(0,2706,100)).astype(int),:]

r = '['
g = '['
b = '['
for ii in range(100):
    r += str(i[ii, 0]) + ', '
    g += str(i[ii, 1]) + ', '
    b += str(i[ii, 2]) + ', '
r = r[:-2]
g = g[:-2]
b = b[:-2]
r += ']'
g += ']'
b += ']'

