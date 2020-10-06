import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('state_crime.csv')

x = [i for i in range(1960,2013)]
y1 = []
y2 = []

for i in range(1960, 2013):
    
    year = df[df['Year']==i][['Data.Rates.Property.All','Data.Rates.Violent.All']]
    theMean = np.mean(year)
    y1.append(theMean['Data.Rates.Property.All'])
    y2.append(theMean['Data.Rates.Violent.All'])

plt.plot(x, y1, color='blue', label='Property Crime')
plt.plot(x, y2, color='red', label='Violent Crimes')
plt.legend()
plt.show()
