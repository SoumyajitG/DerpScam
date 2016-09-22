import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(1337)

lat = []
lon = []

data= open('../data/image_names.txt')

for line in data:
        pt = line.split('_')
        slat,slong = pt[0:2]
        ilat = float(slat)
        ilong = float(slong)
        lat.append(ilat)
        lon.append(ilong)


X = lat
Y = lon

Z = np.vstack((X,Y)).T
print Z.shape
estimators = KMeans(n_clusters=50,n_init=10,n_jobs=16,init='random')



fignum = 1
fig = plt.figure(fignum, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
estimators.fit(Z)
labels = estimators.labels_


ax.scatter(Z[:, 1], Z[:, 0],c=labels.astype(np.float))

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.set_xlabel('Lat')
ax.set_ylabel('Lon')
plt.show()
