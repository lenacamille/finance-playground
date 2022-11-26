import numpy as np
import pandas as pd

# a = np.array([1,2,3,4,5,6,7,8])
# print(np.mean(a))

url = 'cartwheel_data.csv'
df = pd.read_csv(url)

print(type(df))
print(df.head())