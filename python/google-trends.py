import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import pylab as plb

df = pd.read_csv('/Users/d404me/Downloads/google_data.csv')

df_75 = df.tail(int(len(df) * 0.17))

x = 'Week'

y = 'temu'

df_75['Month'] = pd.to_datetime(df_75[x], unit='D', origin = '1899-12-30')


plt.figure(figsize=(10,5), dpi = 200)

plt.plot(df_75['Month'], df_75[y],label ='Search Count', linewidth=2.5)
#
z = np.polyfit(df_75[x], df_75[y] , 1)

p = np.poly1d(z)

plb.plot(df_75['Month'],p(df_75[x]), color = 'purple', linestyle = '-.', label = 'Trendline', linewidth=2.5)


dates = pd.to_datetime([45689, 45749, 45789, 45807, 45819, 45835], unit='D', origin = '1899-12-30')

for i,x_val in enumerate(dates):
    if i == 0:
        plt.axvline(x=x_val, color = 'red', linestyle = '--', label = 'Tariff Announcement')
    else:
        plt.axvline(x=x_val, color = 'red', linestyle = '--')

plt.title('Temu Searches Through the Course of Tariffs', fontsize = 14)

plt.grid(True, 'major')

plt.xlabel('Dates')
plt.ylabel('Search Count')
plt.legend(loc='center', bbox_to_anchor=(0.25, 0.25))

plt.show()
