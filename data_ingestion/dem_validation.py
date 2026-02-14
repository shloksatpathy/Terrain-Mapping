import rasterio
import matplotlib.pyplot as plt

with rasterio.open(r"F:\Terrain Mapping\input-resources\LC09_L2SP_141045_20260130_20260131_02_T1_SR_B3.TIF") as src:
    dem = src.read(1)

plt.imshow(dem, cmap="terrain")
plt.colorbar(label="Elevation (m)")
plt.title("Digital Elevation Model")
plt.show()
