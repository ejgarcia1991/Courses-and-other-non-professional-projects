import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib notebook

MLB=[]
NFL=[]
year=2009
for i in range(8,19):
    row=pd.read_excel('MLB attendance.xlsx',i,skiprows=1,usecols=[10])
    row=row.replace('-',0)
    row=row.sum(axis=0)
    MLB.append([year,row[0]])
    row=pd.read_excel('NFL attendance.xlsx',i,skiprows=1,usecols=[12])
    row=row.replace('-',0)
    row=row.sum(axis=0)
    NFL.append([year,row[0]])
    year+=1

MLB=pd.DataFrame(MLB,columns=['year','Avg'])
NFL=pd.DataFrame(NFL,columns=['year','Avg'])

def percAvgIncrease(row):
    global prev
    global val
    if(prev==None):
        prev=row.Avg
        return 0.
    val= (row.Avg/prev*100)-100
    return val

prev=None
NFL['Avg%Increase']=NFL.apply(percAvgIncrease,axis=1)
prev=None
MLB['Avg%Increase']=MLB.apply(percAvgIncrease,axis=1)



#Plot the data
x=np.arange(11)
NFLavg=NFL['Avg%Increase']
MLBavg=MLB['Avg%Increase']

plt.figure()
plt.plot(x,NFLavg,color='#B83234', linewidth=1)
plt.plot(x,MLBavg,color='#2222AF', linewidth=1)
plt.xticks(x, ('2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'));
plt.xticks(x, ('2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'));
plt.yticks(np.arange(-6,3))
plt.axhline(y=0, color='black', linewidth=1, linestyle='-',alpha=0.5);
#ax = plt.gca()
#ax.fill_between(x, NFLavg, 0, where=NFLavg>=0,facecolor='green', interpolate=True,alpha=0.4)
#ax.fill_between(x, NFLavg, 0, where=NFLavg<0,facecolor='red', interpolate=True,alpha=0.4)

#ax.fill_between(x, MLBavg, 0, where=MLBavg>=0,facecolor='green', interpolate=True,alpha=0.4)
#ax.fill_between(x, MLBavg, 0, where=MLBavg<0,facecolor='red', interpolate=True,alpha=0.4)

#ax.fill_between(x, MLBavg, NFLavg,where=MLBavg>=NFLavg, facecolor='green',interpolate=True, alpha=0.35)
#ax.fill_between(x, MLBavg, NFLavg,where=MLBavg<NFLavg, facecolor='red',interpolate=True, alpha=0.35)

#plt.xlabel('Date', fontsize=10)
plt.ylabel('% increase in attendance', fontsize=10)
plt.title('Attendance comparison between NFL and MLB in the US', fontsize=12)

plt.legend(['NFL attendance','MLB Attendance'],loc=0,frameon=False);