# Importing two other files, so that this one file can call them.
import EV_Data_Story_Project as ev
import EV_Data_Story_AZ_drought as az
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

# Assigning variables to important paths and/or data files.
pathname = '/Users/averyrubins/data/ev228_data/'
file = 'LeesFerryNatlFlow.mon.nc'
file2 = 'USDM-Arizona.csv'
# func1 = ev.lees_ferry(pathname, file)
# func2 = az.az_drought(pathname, file2)

# Calling the functions from both files here.
ev.lees_ferry(pathname, file)
az.az_drought(pathname, file2)
plt.show()
###def lees_ferry(pathname, file):
    ###da = xr.open_dataarray(pathname + file)
    ###print(da)

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
    ###da_timemn = da.groupby('time.year').mean()
    # print('da_timemn', da_timemn)
    ## da_timemn.plot()
    ###return da_timemn


###def az_drought(pathname, file2):
    ###df = pd.read_csv(pathname + file2)

    # Before we craft a figure from this data, let's print it to see what we're working with.
    ###print(df)

    # Extracting D2 (Severe Droughts) and Map Dates, and assigning them to variables.
    ###AZ_drought = df['D2']
    ###dates = df['MapDate']
    # The line of code containing the 'datesmn' variable was our attempt at trying to remove decimals from the dates.
    # It didn't work though.
    # datesmn = dates.groupby('time.year').mean()

    # Our attempt at calculating a trendline here.
    # trend_coefficients = np.ployfit(dates, AZ_drought, 1)
    # trend_function = np.ploy1d(trend_coefficients)

    # Our attempt at ploting the trendline here.
    # plt.plot(dates, trend_function(dates), "r--", label='Trendline')

    # Now we can begin to craft a figure to represent out data, and expand from there.
    # We tried to lower the variability of this data by zooming in to closer intervals in the data.
    ###plt.plot(dates, AZ_drought, color='orange')
    ## plt.xlim(dates[563], dates[0])
    ###return(dates, AZ_drought)

###fig, ax = plt.subplots(1, 2)
###x, y = az_drought(pathname, file2)
###ax[0].plot(x, y)
###x1 = lees_ferry(pathname, file)
###ax[1].plot(x1)
### print(x1.groupby.keys())
###plt.show()