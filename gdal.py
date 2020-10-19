import os
from pathlib import Path

from django.contrib.gis.gdal import DataSource

import world

os.environ['PROJ_LIB'] = r'C:\Users\am\miniconda3\Library\share\proj'

world_shp = str(Path(world.__file__).resolve().parent / 'data' / 'TM_WORLD_BORDERS-0.3.shp')
ds = DataSource(world_shp)
print("Data source        :", ds)
print("Layer amount       :", len(ds))
layer = ds[0]
print("Layer name         :", layer)
print("Layer geometry type:", layer.geom_type)
print("Feature amount     :", len(layer))
print("\nSpatial Reference:\n", layer.srs)
print("\nFields:\n", layer.fields)
print("\nOGR types:\n", [fld.__name__ for fld in layer.field_types])
print("\nFeatures and num points (first 5):")
for feat in layer[0:5]:
    print(feat.get('NAME'), feat.geom.num_points)
print("\nGermany and UN code by idx (71):", layer[71].get("NAME"), layer[71].get("UN"))
feature_germany = layer[71]
geom = feature_germany.geom
# print(geom.wkt)
# print(geom.json)


