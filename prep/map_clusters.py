import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
import matplotlib.patheffects as patheffects
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets
import sys
import pickle

if len(sys.argv) < 2:
	print 'Use: python map_clusters.py <n_clusters>'
	sys.exit()

np.random.seed(1337)

lat = []
lon = []
names = []

data= open('../data/france_streetview_train.txt')

for line in data:
        pt = line.split('_')
        slat,slong = pt[0:2]
        ilat = float(slat)
        ilong = float(slong)
        lat.append(ilat)
        lon.append(ilong)
	names.append(line)

X = lat
Y = lon

Z = np.vstack((X,Y)).T
print Z.shape
num_clusters = int(sys.argv[1])

estimators = pickle.load(open('/work/03699/louisly/local/geolocate/models/cluster100/estimators100.pickle'))
print estimators

#estimators = KMeans(n_clusters=num_clusters,n_init=16,n_jobs=16,init='random')

predictions = estimators.predict(Z)

clusterlabel = np.arange(num_clusters)
cluster_centers = estimators.cluster_centers_

def onpick3(event):
	ind = event.ind
        print 'onpick3 scatter:', ind, np.take(Z[:,1], ind), np.take(Z[:,0], ind), np.take(predictions, ind) 

# commands for getting dense point mapping
plt.figure(1)
ax1 = plt.subplot(111)
plt.scatter(Z[:,1],Z[:,0],s=5,c=predictions.astype(np.float))
#plt.show()

# commands for getting point and click cluster values
#fig = figure()
#ax1 = fig.add_subplot(111)
#col = ax1.scatter(Z[:,1], Z[:,0],predictions, c=predictions.astype(np.float), picker=True)
#fig.canvas.mpl_connect('pick_event', onpick3)

# commands for plotting cluster locations
for i in range(num_clusters) :
	plt.annotate(str(i),(cluster_centers[i,1],cluster_centers[i,0]),color='white',fontsize=15,path_effects=[patheffects.Stroke(linewidth=3,foreground='black'),patheffects.Normal()])
ax1.set_xlabel('Latitude')
ax1.set_ylabel('Longitude')
plt.show()

