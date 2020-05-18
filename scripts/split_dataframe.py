#!/usr/bin/env python3

import geopandas as gpd
import pandas as pd

def split_dataframe(dataframe, n=None, col_name=None):
    if isinstance(dataframe, pd.DataFrame):
        pass
    elif isinstance(dataframe, str):
        print('string')
    else:
        print('data type error')
    print('aaa')

if __name__ == '__main__':
    dataframe = gpd.read_file('../../data/gsi_go_jp/gm-jpn-all_u_2_2/polbnda_jpn.shp')
    split_dataframe(dataframe=dataframe,
                    n=4)
