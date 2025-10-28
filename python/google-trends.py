import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import pylab as plb

df = pd.read_csv('/Users/d404me/Downloads/google_data.csv')

df_75 = df.tail(int(len(df) * 0.17))

x = 'Week'

y = 'temu'




plt.figure(figsize=(10,5), dpi = 200)

ax = df_75.plot(x, y , ax=plt.gca(), label ='Search Count')

z = np.polyfit(df_75[x], df_75[y] , 1)

p = np.poly1d(z)

plb.plot(df_75[x],p(df_75[x]), color = 'purple', linestyle = '-.', label = 'Trendline')


for i,x_val in enumerate([45689, 45749, 45789, 45807, 45819, 45835]):
    if i == 0:
        plt.axvline(x=x_val, color = 'red', linestyle = '--', label = 'Tariff Announcement')
    else:
        plt.axvline(x=x_val, color = 'red', linestyle = '--')

plt.title('Temu Searches Through the Course of Tariffs')

plt.xlabel('Date Number')
plt.ylabel('Search Count')
plt.legend(loc='center', bbox_to_anchor=(0.25, 0.2))
