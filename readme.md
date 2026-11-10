# Terrain Mapping

A Python GIS project for ingesting satellite imagery and elevation data, deriving vegetation indices, and generating 3D terrain meshes.

The current focus is a **data ingestion pipeline** that reads Landsat and SRTM rasters, extracts metadata, and produces analysis-ready layers (NDVI, RGB composites, normalised DEMs). The longer-term goal is a Python library for coordinate handling and texture-mapped 3D mesh generation.

## Features

- Raster metadata extraction (bands, size, bounds, CRS, affine transform)
- True-colour RGB composite from Landsat bands
- NDVI (Normalised Difference Vegetation Index) map
- Multi-temporal NDVI change detection (ΔNDVI between two dates)
- DEM cleaning and normalisation
- Interactive 3D terrain visualisation with PyVista

## Project structure

```
Terrain-Mapping/
├── data_ingestion/
│   ├── meta_data.py          # Extract raster metadata to data.txt
│   ├── RGB_composite.py      # True-colour composite (B4, B3, B2)
│   ├── ndvi.py               # NDVI from Red (B4) and NIR (B5)
│   ├── del_ndvi.py           # NDVI difference between two dates
│   ├── dem_validation.py     # Quick raster/DEM plot
│   ├── dem_normalisation.py  # Clean and normalise SRTM DEM
│   └── 3D_mesh.py            # 3D terrain mesh from the normalised DEM
├── input-resources/          # Raw data (not tracked, see below)
├── requirements.txt
└── readme.md
```

## Setup

Requires Python 3.10+.

```bash
git clone https://github.com/shloksatpathy/Terrain-Mapping.git
cd Terrain-Mapping
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Dependencies: `rasterio`, `numpy`, `matplotlib`, `pyvista`.

## Input resources

Satellite and elevation data is not stored in this repo because of its size (~1.4 GB).
Download it yourself and place it in an `input-resources/` folder at the repo root (it is git-ignored).

**Landsat 8/9 Collection 2 Level-2 (path 141, row 045)** – from [USGS EarthExplorer](https://earthexplorer.usgs.gov/)

| Scene ID | Files used |
|---|---|
| `LC09_L2SP_141045_20260130_20260131_02_T1` | SR bands B1–B7, ST bands, QA, MTL/ANG metadata |
| `LC09_L2SP_141045_20260114_20260116_02_T1` | SR bands B2–B5 |
| `LC08_L2SP_141045_20260122_20260130_02_T1` | SR band B1, ANG metadata |

**SRTM DEM tiles** – from [USGS EarthExplorer](https://earthexplorer.usgs.gov/) (Digital Elevation → SRTM)

| Tile | Formats |
|---|---|
| `n21_e083_3arc_v2` | GeoTIFF (used by `dem_normalisation.py`) |
| `n21_e083_1arc_v3` | GeoTIFF / DTED / BIL |
| `n00_e006_1arc_v3` | GeoTIFF / DTED / BIL |

`del_ndvi.py` also reads Landsat scenes `LC08_L2SP_140044_20251230_20260106_02_T1` and
`LC09_L2SP_140044_20250629_20250630_02_T2` (bands B4, B5) from `data_ingestion/raw/day_0` and `data_ingestion/raw/day_1`.

> **Note:** scripts currently use absolute Windows paths (`F:\Terrain Mapping\...`). Update them to match where you put the data.

## Usage

Run scripts from inside `data_ingestion/`:

```bash
cd data_ingestion
python meta_data.py
python RGB_composite.py
python ndvi.py
python del_ndvi.py
python 3D_mesh.py
```

### `meta_data.py`
Extracts metadata from a TIF file and writes it to `data.txt`:
1. File name
2. Number of bands
3. Width and height
4. Bounds of the raster
5. Affine transform matrix
6. Coordinate reference system (CRS)

### `RGB_composite.py`
Stacks Red (B4), Green (B3) and Blue (B2) into a true-colour image, stretched between the 2nd and 98th percentiles for display.

### `ndvi.py`
Computes NDVI = (NIR − Red) / (NIR + Red) using B5 and B4, and plots it with a red-yellow-green colour map. Values near +1 indicate dense vegetation; values near 0 or below indicate bare soil, built-up areas or water.

### `del_ndvi.py`
Computes NDVI for two acquisition dates and plots their difference (ΔNDVI) to highlight vegetation change over time.

### `dem_validation.py`
Plots a raster with a terrain colour map for quick visual inspection.

### `dem_normalisation.py`
Loads the SRTM DEM, masks nodata and out-of-range elevations (below −1000 m or above 9000 m), and normalises it. Exposes `dem_norm` for other scripts.

### `3D_mesh.py`
Builds a PyVista structured grid from `dem_norm`, applies 30× vertical exaggeration, and opens an interactive 3D viewer.

## Roadmap

- [x] Metadata extraction
- [x] RGB composite
- [x] NDVI and multi-temporal ΔNDVI
- [x] DEM normalisation and 3D mesh
- [ ] Relative paths / config for input data
- [ ] Coordinate-aware mesh generation
- [ ] Texture mapping (drape RGB/NDVI onto the 3D terrain)
- [ ] Package as a reusable Python library
