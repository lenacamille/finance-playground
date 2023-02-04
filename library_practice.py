import numpy as np
import pandas as pd

# a = np.array([1,2,3,4,5,6,7,8])
# print(np.mean(a))

#### IMPORTING THE DATA
url = 'cartwheel_data.csv'
df = pd.read_csv(url)
# We created a pandas dataframe object. 
print(type(df))

#### VIEWING THE DATA

# This prints the first 5 rows. Good for getting a feel for the data.
print(df.head())

# This prints the whole dataframe. Not recommended for large datasets.
# print(df)

# Show a list of the column names
print(df.columns)

# Show the numver of rows and columns in the data
print(df.shape)

# Let's splice up the data
# print(df.loc(0,'Height'))

# import statistics
# year1_data = [-15.6,7.8,5.3,-2.4,-4.0,5.3,-2.1,1.8,3.2,4.2,-2.2]
# print(statistics.median(year1_data),statistics.mode(year1_data))