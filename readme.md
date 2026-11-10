This is my first project on GIS.

Firstly we will focus on develop a data ingestion pipeline for processing satellite data and save and modify insightful data from the ingested data 

on furthur advancements we will be working on devloping a python library for data cordinates and testured mapped 3D mesh generation


*meta_data.py*
{
    this file tends to extract the meta data from a tif file 

    meta data extracted include the :-
    1) name of the tif file
    2) number of bands in the tif file 
    3) height and width of the tif file
    4) the centre of the cordinate reference system 
    5) the affine transform matrix for the tif file  
}


## Input resources

Satellite and elevation data is not stored in this repo because of its size (~1.4 GB).
Download it yourself and place it in an `input-resources/` folder at the repo root (it is git-ignored).

**Landsat 8/9 Collection 2 Level-2 (path 141, row 045)** - from [USGS EarthExplorer](https://earthexplorer.usgs.gov/)
- `LC09_L2SP_141045_20260130_20260131_02_T1` - all SR bands (B1-B7), ST bands, QA and MTL/ANG metadata
- `LC09_L2SP_141045_20260114_20260116_02_T1` - SR bands B2-B5
- `LC08_L2SP_141045_20260122_20260130_02_T1` - SR band B1 and ANG metadata

**SRTM DEM tiles** - from [USGS EarthExplorer](https://earthexplorer.usgs.gov/) (Digital Elevation > SRTM)
- `n21_e083_1arc_v3` and `n21_e083_3arc_v2` (GeoTIFF / DTED / BIL)
- `n00_e006_1arc_v3` (GeoTIFF / DTED / BIL)

`del_ndvi.py` also reads Landsat scenes `LC08_L2SP_140044_20251230_20260106_02_T1` and
`LC09_L2SP_140044_20250629_20250630_02_T2` (bands B4, B5) from `data_ingestion/raw/day_0` and `day_1`.
