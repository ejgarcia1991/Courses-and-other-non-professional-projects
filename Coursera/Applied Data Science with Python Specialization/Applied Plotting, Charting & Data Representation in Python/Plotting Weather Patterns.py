import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df['Data_Value']*=0.1 #Celsius conversion
df['Date'] = pd.to_datetime(df['Date']) #Utility type conversion
df['Year'] = df['Date'].dt.year #Separate year
df['Month_Day'] = df['Date'].dt.strftime('%m-%d') #Separate month and day
df=df[df['Month_Day']!='02-29'] #Remove leap day as stated
df=df.drop('ID',axis=1) #Remove ID as it's of no use

#Get the maximum and minimum temperature for each day and month between 2005 and 2015
maxTemp = df[(df['Year'] >= 2005) & (df['Year'] < 2015) & (df['Element'] == 'TMAX')].groupby(['Month_Day'])['Data_Value'].max()
minTemp = df[(df['Year'] >= 2005) & (df['Year'] < 2015) & (df['Element'] == 'TMIN')].groupby(['Month_Day'])['Data_Value'].min()

df = df.merge(maxTemp.reset_index(drop=False).rename(columns={'Data_Value':'MaxTemp'}), on='Month_Day', how='left')
df = df.merge(minTemp.reset_index(drop=False).rename(columns={'Data_Value':'MinTemp'}), on='Month_Day', how='left')

#Get the values of temperature of 2015 above the past decade
record_high = df[(df['Year']==2015)&(df['Data_Value'] > df['MaxTemp'])]
record_low = df[(df['Year']==2015)&(df['Data_Value'] < df['MinTemp'])]

#Get the maximum and minimum of those values per date
highs=record_high.groupby(['Date'])['Data_Value'].max().reset_index(drop=False)
lows=record_low.groupby(['Date'])['Data_Value'].min().reset_index(drop=False)

#clean up a bit the original dataframe
df=df.sort_values('Month_Day')
df=df.drop_duplicates('Month_Day')
lineData=df[['Month_Day','MaxTemp','MinTemp']]

#At this moment we got a clean dataframe containing the maximum and minimum temperature of each day between 2005-2015
#AND the biggest/minimum values of 2015 that go above those maximum and minimum with their dates 
#so plotting the data is the next step
%matplotlib notebook
%matplotlib inline
import numpy as np

date_index = np.arange('2015-01-01','2016-01-01', dtype='datetime64[D]') #generate the dates for a nice view on the X Axis

#Plot the data
plt.figure()
plt.plot(date_index,maxTemp,color='#B83234', linewidth=1)
plt.plot(date_index,minTemp,color='#2222AF', linewidth=1)
plt.scatter(highs['Date'].values, highs['Data_Value'].values, color='red',s=12)
plt.scatter(lows['Date'].values, lows['Data_Value'].values, color='blue',s=12)

#Get axis from the artist layer
ax = plt.gca()
ax.axis(['2015/01/01','2015/12/31',-40,45]) #fix the range
ax.fill_between(date_index, maxTemp, minTemp, facecolor='#661166', alpha=0.35) #apply the fill

#Extra filler data
plt.xlabel('Date', fontsize=10)
plt.ylabel('‹ Celsius', fontsize=10)
plt.title('Temperature in Ann Arbour, Michigan (2005-2015)', fontsize=12)

plt.legend(['Record high (2005-2014)','Record low (2005-2014)','Record breaking high in 2015','Record breaking low in 2015'],loc=0,frameon=False)

#Fixing the X Axis with month names
#ax.xaxis.set_major_locator(dates.MonthLocator())
#ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))

#ax.xaxis.set_major_formatter(ticker.NullFormatter())
#ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))

for item in ax.xaxis.get_ticklabels():
    item.set_rotation(45)