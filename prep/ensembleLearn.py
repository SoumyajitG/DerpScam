import numpy as np
from sklearn import linear_model

# replace with coarse grained result
bigEstimates = np.array([[.1,.1,.8],[.3,.6,.1],[.2,.6,.2],[.7,.1,.2]])

# replace with fine grained result
littleEstimates = np.array([[.1,.1,.2,.4,.2],[.2,.3,.3,.1,.1],[.2,.1,.1,.2,.6],[.1,.1,.5,.1,.2]])

# replace with target fine grained result
littleTargets = np.array([[0,0,0,1,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,1,0,0]])

inputX = np.hstack((bigEstimates,littleEstimates))
print inputX
print littleTargets.T

for i in range(0, len(littleTargets[0])):
	if sum(littleTargets.T[i]) == 0:
		continue
	logreg = linear_model.LogisticRegression(C=1e5)
	logreg.fit(inputX, littleTargets.T[i])
	print logreg.predict(inputX)
