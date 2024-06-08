import numpy as np
#a = np.array([1,2,3])
#print(a)
#print(type(a))
#print(a.shape)

#b= np.array([[1,2,3],[4,5,6]])
#print(b)
#print(b.shape)

import matplotlib.pyplot as plt

#x= np.arange(0,3*np.pi,0.1)
#y=np.sin(x)
#plt.plot(x,y)
#plt.show()

#x= np.arange(0,3*np.pi,0.1)
#y_sin=np.sin(x)
#y_cos=np.cos(x)
#y_tan=np.tan(x)
#plt.plot(x,y_sin)
#plt.plot(x,y_cos)
#plt.plot(x,y_tan)
#plt.show()

#plt.ylabel('y axis label')
#plt.title('sine and cosine graph')
#plt.legend(['sin','cos'])
#plt.show()

import pandas as pd
df = pd.read_csv('train.csv')
#print(data.head())

import folium
from folium import plugins

stationArr = df[['Y','X']].values

m= folium.Map(location=[stationArr[0][0], stationArr[0][1]], zoom_start=12)
m.add_child(plugins.HeatMap(stationArr[:50000], radius=15))
m.save('abc.html')