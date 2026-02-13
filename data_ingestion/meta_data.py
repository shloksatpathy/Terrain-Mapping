import rasterio 

dataset = rasterio.open("F:\Terrain Mapping\input-resources\LC09_L2SP_141045_20260114_20260116_02_T1_SR_B2.TIF")

data = [
    dataset.name,
    dataset.count,
    dataset.width,
    dataset.height,
    dataset.bounds,
    dataset.transform,
    dataset.crs,
]

try:
    with open("data.txt", 'w', encoding = "utf-8") as f:
        for val in data:
            f.write(str(val))
    print("Meta data written sucessfully into the text file.....")

except OSError as e:
    print(f"Error writing to the file:{e}") 
    
print(data)