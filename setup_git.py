import numpy as np
import pandas as pd
import xarray as xr

temp = 15 + 8 * np.random.randn(2, 2, 3)

precip = 10 * np.random.rand(2, 2, 3)

lon = [[-99.83, -99.32], [-99.79, -99.23]]

lat = [[42.25, 42.21], [42.63, 42.59]]

# for real use cases, its good practice to supply array attributes such as
# units, but we won't bother here for the sake of brevity
ds = xr.Dataset({
                 'precipitation': (['x', 'y', 'time'], precip)},
                 coords={'lon': (['x', 'y'], lon),
                        'lat': (['x', 'y'], lat),
                       'time': pd.date_range('2014-09-06', periods=3),
                        'reference_time': pd.Timestamp('2014-09-05')},
                attrs={'longName':'precipitation','Units':'1.0'})

# ds.attrs['title']= ['precipitation']
ds.to_netcdf('save_disk.nc',encoding={'precipitation': {'dtype': 'int16', 'scale_factor': 0.1, 'zlib': True}})

##
from netCDF4 import Dataset
loadFile = Dataset('save_disk.nc','r')