# Importing the necessary data packages to analyze, plot, and edit our data here.
# Importing seaborn was crucial to help plot a trendline on the figure generated from this file.
import sys
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import pandas as pd
import seaborn as sns

# Writing a function that helps read our data, and then the function will graph it as a figure.
def lees_ferry(pathname, file):
    da = xr.open_dataarray(pathname + file)
    print(da)

    # The following code is our attempt at making a figure of our data using 'index'
    # Note: The comments below is the code that we wrote before integrating it into a function.
    # ds_var_index = ds_var.isel(value=0)
    # ds_var_index.plot()
    # plt.show()
    # da.plot()
    # plt.show()

    # Making a figure that averages the streamflow from each month of each year in the data.
    # This helps lower the variability in the figure, making it easier to read.
    da_timemn = da.groupby('time.year').mean()
    print('da_timemn', da_timemn)
    # The sys.exit('STOP') code was added so that we could stop the code when we experienced any troubleshoots.
    # sys.exit('STOP')

    # The print(da_timemn.data) function below was necessary so that we could see what our streamflow values were now, before plotting this data as a figure.
    print(da_timemn.data)

    # This code is what plots the data as a figure, as well as adding a trendline and name to it, allowing us to show two figures at the same time.
    plt.figure(1)
    sns.regplot(x=da_timemn['year'].data, y=da_timemn.data, line_kws={'color':'red'}, scatter=False)
    plt.plot(da_timemn['year'].data, da_timemn.data, label='Lees Ferry Stream Flow', color='blue')
    plt.xlabel('Years')
    plt.ylabel('Average Streamflow (ft per month)')
    plt.title('Streamflow in Lees Ferry from 1905-2017')
    plt.xlim(1905, 2017)

    