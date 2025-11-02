# Importing the necessary packages before creating a figure.
# We probably won't need to use numpy for this code, but it's there in case we do.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating a path to the folder containing the data we want to analyze.


# Importing this Arizona drought data here.
# The reason why we are importing Arizona drought data is because Lee's Ferry is located in Arizona.
# Therefore, by importing this data, it will still somewhat related to Lee's Ferry.
def az_drought(pathname, file2):
    df = pd.read_csv(pathname + file2)

    # Before we craft a figure from this data, let's print it to see what we're working with.
    # print(df)

    # Extracting D2 (Severe Droughts) and Map Dates, and assigning them to variables.
    AZ_drought = df['D2']
    dates = df['MapDate']

    # Our attempt at calculating a trendline here.
    # trend_coefficients = np.ployfit(dates, AZ_drought, 1)
    # trend_function = np.ploy1d(trend_coefficients)

    # Our attempt at ploting the trendline here.
    # plt.plot(dates, trend_function(dates), "r--", label='Trendline')

    # Now we can begin to craft a figure to represent out data, and expand from there.
    # We tried to lower the variability of this data by zooming in to closer intervals in the data.
    plt.plot(dates, AZ_drought, color='orange')
    plt.xlim(dates[563], dates[0])
    plt.xlabel('Years')
    plt.ylabel('AZ in Severe Drought (%)')
    plt.title('Percentage of Severe Drought in AZ')
    plt.show()