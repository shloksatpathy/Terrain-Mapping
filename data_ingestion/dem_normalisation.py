import rasterio
import numpy as np
with rasterio.open(r"F:\Terrain Mapping\input-resources\n21_e083_3arc_v2.tif") as src:
    dem = src.read(1).astype(np.float32)

    nodata = src.nodata


if nodata is not None:
    dem[dem == nodata] = np.nan

#guard against extreme values 
dem[dem < -1000] = np.nan
dem[dem > 9000] = np.nan



# Normalize elevation
dem_norm = (dem - np.nanmin(dem)) / np.nanmax(dem) - np.nanmin(dem)

dem_norm = np.nan_to_num(dem_norm)

print("DEM shape:", dem_norm.shape)
