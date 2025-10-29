# This file is for practicing writing code for our Environmental Data Story project.
# We were given .nc data, which is gridded.
# With this file, we will practice analyzing our data as a csv file.
# Remember to activate 'ev228' before running this code, otherwise it won't work as intended.

# Importing relevant packages for analyzing a csv file.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Variables including the path to the correct folder that contains the right file.
path = '/Users/jamespatla/ev228_data/'
filename = 'LeesFerryNatlFlow.mon.csv'

# Code for importing our data here.
df = pd.read_csv(path + filename)

# Print our data variable here.
# Note: If any results we get are '-9999.0', this means that there is a missing vaule in the data, and that's fine.
print(df)