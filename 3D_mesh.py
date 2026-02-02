import pyvista as pv
import numpy as np 
from dem_normalisation import dem_norm

ny, nx = dem_norm.shape
x = np.arange(nx)
y = np.arange(ny)
x, y = np.meshgrid(x, y)

grid = pv.StructuredGrid(
    x.astype(np.float32),
    y.astype(np.float32),
    dem_norm.astype(np.float32)
)

# Controlled exaggeration
grid.points[:, 2] *= 30

plotter = pv.Plotter()
plotter.add_mesh(grid, cmap="terrain", show_edges=False)
plotter.show()
