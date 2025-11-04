# Importing the necessary data packages to analyze our data.
import sys

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import pandas as pd
import seaborn as sns

# Will start to make a variable with the path to our data, once we've leanred more about working with gridded data.

# Write a function that sets a variable to a bound method, which helps read our data, and then the function will graph it as a figure.
def lees_ferry(pathname, file):
    da = xr.open_dataarray(pathname + file)
    print(da)

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
    print('da_timemn', da_timemn)
    # sys.exit('STOP')

    print(da_timemn.data)
    plt.figure(1)
    sns.regplot(x=da_timemn['year'].data, y=da_timemn.data, line_kws={'color':'red'}, scatter=False)
    plt.plot(da_timemn['year'].data, da_timemn.data, label='Lees Ferry Stream Flow', color='blue')
    plt.xlabel('Years')
    plt.ylabel('Average Streamflow (ft per month)')
    plt.title('Streamflow in Lees Ferry from 1905-2017')
    plt.xlim(1905, 2017)
    # plt.show()
    

    # df = pd.read_csv(pathname + file2)
    # AZ_drought = df['D2']
    # dates = df['MapDate']

    # Plotting lines for both data sets.
    # plt.figure(figsize=(10, 6))
    # plt.plot(da_timemn, label='Lees Ferry Stream Flow')
    # plt.plot(dates, AZ_drought, label='Arizona Drought Data')
    # plt.title('Relationship Between NetCDF and CSV')
    # plt.legend()
    # plt.show()

    