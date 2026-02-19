import rasterio
import numpy as np 
import matplotlib.pyplot as plt

#first we will calculate the two NDVI's for the different dates 
#then we will calculate the difference betweeen them to find 
#delNDVI as (NDVI_1 - NDVI_2)
class NDVI_1 :
    red = rasterio.open("F:\Terrain Mapping\input-resources\LC09_L2SP_141045_20260130_20260131_02_T1_SR_B4.TIF").read(1).astype(float)
    nir = rasterio.open("F:\Terrain Mapping\input-resources\LC09_L2SP_141045_20260130_20260131_02_T1_SR_B5.TIF").read(1).astype(float)


    np.seterr(divide='ignore', invalid='ignore')

    ndvi_1 = (red - nir)/(red + nir)




class NDVI_2 :
    red = rasterio.open()
    nir = rasterio.open()

    np.seterr(divide='ignore', invalid='ignore')

    ndvi_2 = (red - nir)/(red + nir)



#plottings for the two classes with the defference

del_ndvi = ndvi_1 = ndvi_2

#plottings

