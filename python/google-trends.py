import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import pylab as plb

# It's important to note that Excel and Google Sheets store dates as a number, where day 1 is 1/1/1900 (In Excel; 12/30/1899 for Google Sheets)
# You can these numbers by switching format, from date format to the number format
# The dates for tariffs can then be easily input and worked into a dataset, since they are treated as a number
# This requires changing the time of your data into the number format
# This makes the process of plotting specific dates - especially when you are given weekly data easier - in my opinion;
# In the following code, the above was done, but the numbers corresponding to certain dates were visually changed back to dates


df = pd.read_csv('/Users/User/Path/google_data.csv')

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
