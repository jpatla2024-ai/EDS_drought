# Importing two other files, so that this one file can call them.
import EV_Data_Story_Project as ev
import EV_Data_Story_AZ_drought as az
import matplotlib.pyplot as plt

# Assigning variables to important paths and/or data files.
pathname = '/Users/jamespatla/ev228_data/'
file = 'LeesFerryNatlFlow.mon (1).nc'
file2 = 'USDM-Arizona.csv'
# func1 = ev.lees_ferry(pathname, file)
# func2 = az.az_drought(pathname, file2)

# Calling the functions from both files here.
ev.lees_ferry(pathname, file)
az.az_drought(pathname, file2)

# Attempting to show both plots in one figure.
# fig, (func1, func2) = plt.subplots(1, 2, figsize=(10, 10))
# axd[func1].set_title('Streamflow in Lees Ferry')
# axd[func2].set_title('Severe Droughts in Arizona')