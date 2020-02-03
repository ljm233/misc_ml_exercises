import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn import cross_validation
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC,LinearSVC,NuSVC


 
train    = pd.read_csv("C:\\Udemy\\Practical Data Science in Python\\Audio\\data_model.csv")
test     = pd.read_csv("C:\\Udemy\\Practical Data Science in Python\\Audio\\validation.csv")

#------------------------------------------------------------------------------------------------#

x = train[["meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent","sfm","mode","centroid",
           "peakf","meanfun","minfun",
       "maxfun","meandom","mindom","maxdom","dfrange","modindx"]]
y = train["class"]
clh = tree.DecisionTreeClassifier(max_depth  = 7)
clf = AdaBoostClassifier(base_estimator= clh,n_estimators=10)
clf.fit(x,y)

print(np.mean(cross_validation.cross_val_score(clf, x, y, cv=8)))
print(confusion_matrix(y, clf.predict(x)))
test_x = test[["meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent","sfm","mode",
               "centroid","peakf","meanfun","minfun",
       "maxfun","meandom","mindom","maxdom","dfrange","modindx"]]
print(clf.score(test_x,test["class"]))

#---------------------------------------------------------------------------#

svcfit = SVC(C=0.01, kernel='linear', gamma='scale')
#x     =  preprocessing.scale(x)

svcfit.fit(x, y)

print(np.mean(cross_validation.cross_val_score(svcfit, x, y, cv=8)))
print(confusion_matrix(y, svcfit.predict(x)))
#test_x     =  preprocessing.scale(test_x)
print(svcfit.score(test_x,test["class"]))

#---------------------------------------------------------------------------#




