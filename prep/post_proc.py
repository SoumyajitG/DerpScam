import pickle
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets

clusterID = 13
estimatorLater = pickle.load(open("estimator.pickle"))
print estimatorLater.cluster_centers_[clusterID]

