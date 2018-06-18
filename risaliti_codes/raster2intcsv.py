import os, sys

from osgeo import gdal
from osgeo import gdalconst

# get the arguments
InRaster = sys.argv[1]
OutCSV   = sys.argv[2]

# open the raster and get some properties
ds       = gdal.OpenShared(InRaster,gdalconst.GA_ReadOnly)
GeoTrans = ds.GetGeoTransform()
ColRange = range(ds.RasterXSize)
RowRange = range(ds.RasterYSize)
rBand    = ds.GetRasterBand(1) # first band
nData    = rBand.GetNoDataValue()
if nData == None:
    nData = -9999 # set it to something if not set
else:
    print("NoData value is {0}".format(nData))

# specify the centre offset
HalfX    = GeoTrans[1] / 2
HalfY    = GeoTrans[5] / 2

with open(OutCSV,'w') as CSVwrite:
    for ThisRow in RowRange:
        RowData = rBand.ReadAsArray(0,ThisRow,ds.RasterXSize,1)[0]
        for ThisCol in ColRange:
            if RowData[ThisCol] != nData:
                if RowData[ThisCol] > 0:
                      CSVwrite.write('{0},{1},{2}\n'.format(ThisCol,ThisRow,RowData[ThisCol])) 


