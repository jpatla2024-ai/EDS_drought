# Importing the necessary data packages to analyze our data.
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

# Will start to make a variable with the path to our data, once we've leanred more about working with gridded data.

# Write a function that sets a variable to a bound method, which helps read our data, and then the function will graph it as a figure.
def lees_ferry(pathname, file):
    da = xr.open_dataarray(pathname + file)
    # ds_var = ds['value']
    # print(ds_var)
    # print(da)

    # The following code is our attempt at making a figure of our data using 'index'
    # Note: The comments below is the code that we wrote before integrating it into a function.
    # This will probably be subjected to change in the future.
    # ds_var_index = ds_var.isel(value=0)
    # ds_var_index.plot()
    # plt.show()
    # da.plot()
    # plt.show()

    # Making a figure that averages the streamflow from each month of each year in the data.
    # This helps lower the variability in the figure, making it easier to read.
    da_timemn = da.groupby('time.year').mean()
    da_timemn.plot()
    plt.xlabel('Years')
    plt.ylabel('Average Streamflow (ft per month)')
    plt.title('Streamflow in Lees Ferry')
    plt.show()