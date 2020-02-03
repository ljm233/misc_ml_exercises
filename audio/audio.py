import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn import preprocessing


# import data for train and test 
train = pd.read_csv('/home/lawrence/udemy/audio/Audio/data_model.csv')
test = pd.read_csv('/home/lawrence/udemy/audio/Audio/validation.csv')


X = train[["meanfreq", "sd", 
			"freq.median", "freq.Q25", "freq.Q75", "freq.IQR", 
			"time.median", "time.Q25", "time.Q75", "time.IQR", 
			"skew", "kurt", "sp.ent", "time.ent", "entropy", "sfm", 
			"meandom", "mindom", "maxdom", "dfrange", "modindx", 
			"startdom", "enddom", "dfslope", "meanpeakf"
]]	
y = train['class']

X_test = test[["meanfreq", "sd", 
			"freq.median", "freq.Q25", "freq.Q75", "freq.IQR", 
			"time.median", "time.Q25", "time.Q75", "time.IQR", 
			"skew", "kurt", "sp.ent", "time.ent", "entropy", "sfm", 
			"meandom", "mindom", "maxdom", "dfrange", "modindx", 
			"startdom", "enddom", "dfslope", "meanpeakf"
]]	
y_test = test['class']


# Classify using adaboost with decision tree
clh = DecisionTreeClassifier(max_depth=10)
clf = AdaBoostClassifier(clh)
clf.fit(X, y)

print('adaboost + dt performance.')
print(np.mean(cross_val_score(clf, X, y, cv=7)))
print(confusion_matrix(y_test, clf.predict(X_test)))
print(clf.score(X_test, y_test), end='\n\n')

# classify using svc
clf = SVC(C=0.01, kernel='linear', gamma='scale')
X = preprocessing.scale(X)
clf.fit(X, y)

print(np.mean(cross_val_score(clf, X, y, cv=8)))
X_test = preprocessing.scale(X_test)
print(confusion_matrix(y_test, clf.predict(X_test)))
print(clf.score(X_test, y_test), end='\n\n')





