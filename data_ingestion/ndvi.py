import rasterio 
import numpy as np 
import matplotlib.pyplot as plt 

red = rasterio.open("F:\Terrain Mapping\input-resources\LC09_L2SP_141045_20260130_20260131_02_T1_SR_B4.TIF").read(1).astype(float)
nir = rasterio.open("F:\Terrain Mapping\input-resources\LC09_L2SP_141045_20260130_20260131_02_T1_SR_B5.TIF").read(1).astype(float)

#avoiding division by 0

np.seterr(divide='ignore', invalid='ignore')

ndvi = (nir - red) / (nir + red)

#plots
plt.imshow(ndvi, cmap = 'RdYlGn')
plt.colorbar(label = "NDVI")
plt.title("NDVI MAP")
plt.show()