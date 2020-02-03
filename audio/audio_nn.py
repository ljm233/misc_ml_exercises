# audio_nn.py

import numpy as np
import pandas as pd

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout

# import data from csv
train = pandas.read_csv('/home/lawrence/udemy/audio/Audio/data_model_nn.csv')
test = pandas.read_csv('/home/lawrence/udemy/audio/Audio/validation_nn.csv')

# split into x and y
X = train[["meanfreq", "sd", 
			"freq.median", "freq.Q25", "freq.Q75", "freq.IQR", 
			"time.median", "time.Q25", "time.Q75", "time.IQR", 
			"skew", "kurt", "sp.ent", "time.ent", "entropy", "sfm", 
			"meandom", "mindom", "maxdom", "dfrange", "modindx", 
			"startdom", "enddom", "dfslope", "meanpeakf"
]]
y = train['class']
oh_y = to_categorical(y, num_classes=5) # one hot encoding

# do same for test
X_test = test[["meanfreq", "sd", 
			"freq.median", "freq.Q25", "freq.Q75", "freq.IQR", 
			"time.median", "time.Q25", "time.Q75", "time.IQR", 
			"skew", "kurt", "sp.ent", "time.ent", "entropy", "sfm", 
			"meandom", "mindom", "maxdom", "dfrange", "modindx", 
			"startdom", "enddom", "dfslope", "meanpeakf"
]]
y_test = test['class']
oh_y_test = y_test(y_test, num_classes=5)



# define and compile model
model = Sequential()
model.add(Dense(10, activation='relu', input_dim=25))
mdel.add(Dropout(0.15))
model.add(Dense(10, activation='relu',))
mdel.add(Dropout(0.15))
model.add(Dense(6, activation='softmax',))
model.compile(	optimizer='rmsprop',
			 	loss='categorical_crossentropy',
			 	metrics=['accuracy']
			 )


# fit model and score
model.fit(X, y, epochs=10, batch_size=5)
score = model.evaluate(x_test, y_test, batch_size=16)
