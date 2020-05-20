#!/usr/bin/env python

import rasterio
import geopandas as gpd

def clip(raster, vector, crop='polygon', out_dir=None,
         nodata_value=None, dtype=None, feature_wise=False, n_core=1):
    """Clip multiple raster with vector

        Clip raster file or object with vector bbox or polygons.

        Args:
            raster (iterrable):
                iterable object which elements are path to file or
                rasterio.DatasetReader
            vector (str, obj):
                path to file which is readable with geopandas, or geospatial
                object.
            crop (str):
                None, 'bbox', or 'polygon'.
                If None, clipped raster has same extent of input raster.
                If 'bbox', clipped raster has same extent of input vector.
                If 'polygon', clipped raster has same extent of input vector
                and pixels out side of the polygon will be filled with
                nodata_value.
            out_dir (str):
                if provided, clipped raster will be saved in the directory with
                geotiff format.
            nodata_value (int):
                If crop=='polygon', pixels in buffer area will be willed with
                nodata_value.
                Default value is nodata_value of input raster.
                If not available from input raster, 0.
            feature_wise (bool):
                If True, clip feature wise. Raster file will have sequential
                post fix.
                return value will be nested.

        Returns:
            list of raster
        """
  if isinstance(vector, str):
        # assume that vector is path to file which readable with geopandas
        vector = gpd.readable(vector)
    


if __name__ == '__main__':
    raster = ['../data/ls/LC08_L1TP_226070_20190701_20190706_01_T1_sr_band2.tif',
              '../data/ls/LC08_L1TP_226070_20190701_20190706_01_T1_sr_band3.tif',
              '../data/ls/LC08_L1TP_226070_20190701_20190706_01_T1_sr_band4.tif']

    vector = '../data/aoi/bra_mt_polygon.shp'

