# Importing two other files, so that this one file can call them.
# We are also importing other necessary packages that we might need, though most of them might not be necessary.
import EV_Data_Story_Project as ev
import EV_Data_Story_AZ_drought as az
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

# Assigning variables to important paths and/or data files.
pathname = '/Users/averyrubins/data/ev228_data/'
file = 'LeesFerryNatlFlow.mon.nc'
file2 = 'USDM-Arizona.csv'

# Calling the functions from both files here.
# Followed up by show the two figures that these functions are plotting.
ev.lees_ferry(pathname, file)
az.az_drought(pathname, file2)
plt.show()