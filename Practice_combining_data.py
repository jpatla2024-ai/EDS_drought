# Importing the necessary data packages to analyze our data.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

# Making variables containing the path and correct data files.
pathname = '/Users/jamespatla/ev228_data/'
file = 'LeesFerryNatlFlow.mon (1).nc'
file2 = 'USDM-Arizona.csv'

# Writing variables that will read our separate datasets, based on what kind of files they are.
# For the Arizona drought data, we are importing it because Lee's Ferry is located in Arizona.
da = xr.open_dataarray(pathname + file)
df = pd.read_csv(pathname + file2)

# Plotting .nc file and .csv file.
# da_timemn = da.groupby('time.year').mean()
# AZ_drought = df['D2']
# dates = df['MapDate']
# plt.plot(da_timemn)
# plt.plot(dates, AZ_drought, color='red')
# plt.show()