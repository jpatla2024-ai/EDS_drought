# Importing the necessary packages before creating a figure, and editing the code here.
# We probably won't need to use numpy for this code, but it's there in case we do.
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Importing our Arizona drought data here.
# The reason why we are importing Arizona drought data is because Lee's Ferry is located in Arizona.
# Therefore, by importing this data, it will still relate to Lee's Ferry.
def az_drought(pathname, file2):
    df = pd.read_csv(pathname + file2)

    # Before we craft a figure from this data, let's print it to see what we're working with.
    print(df)

    # Extracting D2 (Severe Droughts) and Map Dates, and assigning them to variables.
    AZ_drought = df['D2']
    dates = df['MapDate']
    gooddates = pd.to_datetime(dates, format='%Y%m%d')
    print(AZ_drought)
    print(gooddates)
    
    # The next couple lines of comments show code that we wrote when experimenting with different data analysis techniques, specifically trendlines.
    # Although none of this worked, it's still important to show the detail and work that went into this project to make it as functional as possible.
    
    # sys.exit('STOP')
    # The line of code containing the 'datesmn' variable was our attempt at trying to remove decimals from the dates.
    # It didn't work though.
    # datesmn = dates.groupby('time.year').mean()

    # Our attempt at calculating a trendline here.
    # trend_coefficients = np.ployfit(dates, AZ_drought, 1)
    # trend_function = np.ploy1d(trend_coefficients)

    # Our attempt at ploting the trendline here.
    # plt.plot(dates, AZ_drought, '.', trend_function(dates), "r--", label='Trendline')

    # Now we can begin to craft a figure to represent out data, and expand from there.
    # We tried to lower the variability of this data by zooming in to closer intervals in the data.
    plt.figure(2)
    plt.plot(gooddates, AZ_drought, color='orange')
    plt.xlim(gooddates[563], gooddates[0])
    plt.xlabel('Years')
    plt.ylabel('AZ in Severe Drought (%)')
    plt.title('Percentage of AZ in Severe Drought from 2015-2025')