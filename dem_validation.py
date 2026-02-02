import rasterio
import matplotlib.pyplot as plt

with rasterio.open(r"F:\Terrain Mapping\input-resources\n21_e083_3arc_v2.tif") as src:
    dem = src.read(1)

plt.imshow(dem, cmap="terrain")
plt.colorbar(label="Elevation (m)")
plt.title("Digital Elevation Model")
plt.show()
