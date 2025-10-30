# Importing the necessary data packages to analyze our data.
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

# Will start to make a variable with the path to our data, once we've leanred more about working with gridded data.
pathname = '/Users/jamespatla/ev228_data/'
file = 'LeesFerryNatlFlow.mon (1).nc'

# Write code that sets a variable to a bound method, which helps read our data.
da = xr.open_dataarray(pathname + file)
# ds_var = ds['value']
# print(ds_var)
print(da)

# The following code is our attempt at making a figure of our data using 'index'.
# 
# This will probably be subjected to change in the future.
# ds_var_index = ds_var.isel(value=0)
# ds_var_index.plot()
# plt.show()

# da.plot()
# plt.show()
da_timemn = da.groupby('time.year').mean()
da_timemn.plot()
plt.xlabel('Years')
plt.ylabel('Average Streamflow (ft per month)')
plt.title('Streamflow in Colorado Basin')
plt.show()
# np_data = da.data
# da_timemn.plot()
# plt.show()
## print(da_timemn)
# print(list(np_data))