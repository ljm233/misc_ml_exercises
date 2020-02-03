from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import pandas
import numpy as np



# import dataset
data = pandas.read_csv("/home/lawrence/udemy/wines/wine.data", names=['Class', "Alcohol","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"])
y = data['Class'].values
del data['Class']


# determine optimal parameters
clh = DecisionTreeClassifier(max_depth=10)
parameters = {'max_depth':np.arange(1, 10)}
clfx = GridSearchCV(clh, parameters)
clfx.fit(data, y)
print(clfx.best_params_)


# classify wines
clh = DecisionTreeClassifier(max_depth=clfx.best_params_['max_depth'])
clf = AdaBoostClassifier(clh, n_estimators=10)
clf.fit(data, y)


print(np.mean(cross_val_score(clf, data.values, y, cv=4)))