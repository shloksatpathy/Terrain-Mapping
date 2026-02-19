import rasterio
import numpy as np 
import matplotlib.pyplot as plt

#first we will calculate the two NDVI's for the different dates 
#then we will calculate the difference betweeen them to find 
#delNDVI as (NDVI_1 - NDVI_2)
class NDVI_1 :
    red = rasterio.open(r"F:\Terrain Mapping\data_ingestion\raw\day_0\LC08_L2SP_140044_20251230_20260106_02_T1_SR_B4.TIF").read(1).astype(float)
    nir = rasterio.open(r"F:\Terrain Mapping\data_ingestion\raw\day_0\LC08_L2SP_140044_20251230_20260106_02_T1_SR_B5.TIF").read(1).astype(float)

    np.seterr(divide='ignore', invalid='ignore')

    ndvi = (red - nir)/(red + nir)
    plt.imshow(ndvi, cmap = 'RdYlGn')
    plt.colorbar(label = "NDVI")
    plt.title("NDVI MAP")
    plt.show()

class NDVI_2 :
    red = rasterio.open(r"F:\Terrain Mapping\data_ingestion\raw\day_1\LC09_L2SP_140044_20250629_20250630_02_T2_SR_B4.TIF").read(1).astype(float)
    nir = rasterio.open(r"F:\Terrain Mapping\data_ingestion\raw\day_1\LC09_L2SP_140044_20250629_20250630_02_T2_SR_B5.TIF").read(1).astype(float)

    np.seterr(divide='ignore', invalid='ignore')

    ndvi = (red - nir)/(red + nir)
    plt.imshow(ndvi, cmap = 'RdYlGn')
    plt.colorbar(label = "NDVI")
    plt.title("NDVI MAP")
    plt.show()

#plottings for the two classes with the defference

del_ndvi = NDVI_1.ndvi - NDVI_2.ndvi

#plottings
plt.imshow(del_ndvi, cmap = 'RdYlGn')
plt.colorbar(label = "NDVI")
plt.title("NDVI MAP")
plt.show()
