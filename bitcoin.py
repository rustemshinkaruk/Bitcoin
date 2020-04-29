import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import timedelta


bit=pd.read_csv('Bitcoin Historical Data - Investing.com.csv')
bit.Date=bit.Date.map(lambda x: datetime.datetime.strptime(x,'%b %d, %Y'))
bit.Price=bit.Price.str.replace(',', '').astype(float)
bit.set_index('Date',inplace=True)
bit['log_price']=np.log(bit.Price)
bit['index']=np.arange(0,len(bit.Price))

k=150
ret=[]
dates=[2707,1388,0]
for i in dates:
    if i!=0:
        ret.append((bit.Price[i]-bit.Price[i+k])/bit.Price[i+k])
        ret.append((bit.Price[i-k]-bit.Price[i])/bit.Price[i])
    else:
        ret.append((bit.Price[i]-bit.Price[i+k])/bit.Price[i+k])
ret=[str(int(i*100))+'%' for i in ret]
ret
#plt.style.use('default')

ax=plt.subplot()
bit.log_price.plot(ax=ax)
ax.set_yticks(np.arange(-1,10,0.38))
ax.set_yticklabels(['$0.05','$0.20','','$0.50','','$2','','$10','','','$20','','$50',
                    '','$100','','$200','','$500','','$1000','','$2000','','$5000','','$10000',
                    '','$20000'])
ax.set_title("Bitcoin Halving events and returns")
ax.set_ylabel("")
ax.set_xlabel("")

ax.axvline("2012-11-28 00:00:00",alpha=0.4,color='red')
ax.axvline("2016-07-09 00:00:00",alpha=0.4,color='red')
ax.axvline("2020-04-27 00:00:00",alpha=0.4,color='red')


ax.axvspan(bit.index[2707]-timedelta(days=k), "2012-11-28 00:00:00", alpha=0.1, color='orange')
ax.axvspan(bit.index[2707]+timedelta(days=k), "2012-11-28 00:00:00", alpha=0.1, color='orange')

ax.axvspan(bit.index[1388]-timedelta(days=k), "2016-07-09 00:00:00", alpha=0.1, color='orange')
ax.axvspan(bit.index[1388]+timedelta(days=k), "2016-07-09 00:00:00", alpha=0.1, color='orange')

ax.axvspan(bit.index[0]-timedelta(days=k), "2020-04-27 00:00:00", alpha=0.1, color='orange')

ax.annotate(ret[0],xy=(bit.index[int(2707+1.3*k)],bit.log_price[int(2707+k)]+4),
            fontsize=8)
ax.annotate(ret[1],xy=(bit.index[int(2707-0.1*k)],bit.log_price[int(2707+k)]+5),
            fontsize=8)

ax.annotate(ret[2],xy=(bit.index[int(1388+1.3*k)],bit.log_price[int(2707+k)]+5.5),
            fontsize=8)
ax.annotate(ret[3],xy=(bit.index[int(1388-0.1*k)],bit.log_price[int(2707+k)]+6.5),
            fontsize=8)

ax.annotate('0.3%',xy=(bit.index[int(0+1.3*k)],bit.log_price[int(2707+k)]+7.5),
            fontsize=8)



fig = plt.gcf()
fig.set_size_inches(11.5, 7.5)
fig.savefig('bitcoin.png', dpi=100)




#=======================================================================================



ax = plt.subplot(111)
ax.plot(np.arange(2012,2052,4),np.cumsum(210240*50*np.geomspace(1,0.5**9,10)))
ax.set_title("Amount of Bitcoins in universe")
ax.set_ylabel("Number of Bitcoins in 10 millions")

ax2=ax.twinx()
ax2.step(np.arange(2012,2052,4),np.geomspace(50,50*0.5**10,10),color='orange')
ax2.set_ylabel('Amount of Bitcoins per 10 minutes')
ax.legend(('Number of Bitcoins',),loc=2)

ax.set_xlabel('Year')

fig = plt.gcf()
fig.set_size_inches(11.5, 7.5)
fig.savefig('21million.png', dpi=100)



















