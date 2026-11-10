import rasterio 
import numpy as np 
import matplotlib.pyplot as plt 

red = rasterio.open("../input-resources/LC09_L2SP_141045_20260130_20260131_02_T1_SR_B4.TIF").read(1).astype(float)
green = rasterio.open("../input-resources/LC09_L2SP_141045_20260130_20260131_02_T1_SR_B3.TIF").read(1).astype(float)
blue = rasterio.open("../input-resources/LC09_L2SP_141045_20260130_20260131_02_T1_SR_B2.TIF").read(1).astype(float)

#stacking of float values as RGB pixels
rgb = np.dstack((red, green, blue))

# Normalize for display
rgb_min = np.percentile(rgb, 2)
rgb_max = np.percentile(rgb, 98)
rgb = np.clip((rgb - rgb_min) / (rgb_max - rgb_min), 0, 1)


#plottings
plt.imshow(rgb)
plt.title("RGB composite")
plt.axis("off")
plt.show()
