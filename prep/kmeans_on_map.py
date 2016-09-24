import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

import os
import pickle
from sklearn.cluster import KMeans
from sklearn import datasets

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
estimators = KMeans(n_clusters=50,n_init=10,n_jobs=16,init='random')

#fignum = 1
#fig = plt.figure(fignum, figsize=(4, 3))
#plt.clf()
#ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

#plt.cla()
predictions = estimators.fit_predict(Z)

pickleFile = open('estimator.pickle','wb')
pickle.dump(estimators,pickleFile)
pickleFile.close()

# for later
# estimatorLater = pickle.loads(pickleFile)?

with open('thedata.txt','w') as f:
	for i in range(0,len(names)):
		f.write(names[i][:-1] + ' ' + str(predictions[i]) + '\n')

# create lmdb
os.system('convert_imageset -backend=lmdb --resize_height=224 --resize_width=224 /scratch/03173/soumyag/DerpScam/france_streetview/ thedata.txt train_lmdb')

# don't need mean file after all
#os.system('compute_image_mean -backend=lmdb train_lmdb mean.binaryproto')




#ax.scatter(Z[:, 1], Z[:, 0],c=labels.astype(np.float))

#ax.w_xaxis.set_ticklabels([])
#ax.w_yaxis.set_ticklabels([])
#ax.set_xlabel('Lat')
#ax.set_ylabel('Lon')
#plt.show()
