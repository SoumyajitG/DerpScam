import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
import sys
import pickle
import os.path

if len(sys.argv) < 2:
	print 'Use: python test.py <estimator.pickle> <cnn_outputs>'
	sys.exit()

np.random.seed(1337)

estimator_pickle = str(sys.argv[1])
cluster_centers_f = 'cc_' + estimator_pickle
if os.path.isfile(cluster_centers_f):
	print 'loading existing cluster centers file'
	with open(cluster_centers_f) as ccpf:
		cluster_centers = pickle.load(ccpf)
else:
	with open(estimator_pickle) as epf:
		estimators = pickle.load(epf)	
		print 'writing new cluster centers file'
		cluster_centers = estimators.cluster_centers_
		with open(cluster_centers_f,'wb') as ccpf:
			pickle.dump(cluster_centers,ccpf)

num_clusters = cluster_centers.shape[0]
print num_clusters

if len(sys.argv) < 3:
        print 'Use: python test.py <estimator.pickle> <cnn_outputs>... using random outputs:'
        cnn_outputs = np.random.dirichlet(np.full(num_clusters,1.0), 1)[0]
#	print cnn_outputs
else:
        cnn_outputs = sys.argv[2]

def getEstLatLon(cnn_outputs, cluster_centers, estType):
	if estType == 0: # choose best cluster
		best_cluster = np.argmax(cnn_outputs)
		return cluster_centers[best_cluster]
	if estType == 1: # choose weighted average of clusters
		return np.dot(cnn_outputs,cluster_centers)
	if estType == 2: # choose penalized weighted average of clustersi
		rewgt = np.square(cnn_outputs)
		rewgt_outputs = rewgt / np.sum(rewgt)
		return np.dot(rewgt_outputs,cluster_centers)

print 'all clusters mean: ' + str(np.mean(cluster_centers,0))
print 'most likely cluster center: ' + str(getEstLatLon(cnn_outputs, cluster_centers, 0))
print 'weighted estimate of lat/lon: ' + str(getEstLatLon(cnn_outputs, cluster_centers, 1))
print 'penalized estimate of lat/lon: ' + str(getEstLatLon(cnn_outputs, cluster_centers, 2))
