#----------- Importing dataset -----------#

import pandas as pd
glass_data = pd.read_csv('./glass.csv')

#Preprocessing data
x=glass_data.drop('Type',axis=1)
y=glass_data['Type']


#----------Splitting Data-----------#
# Import train_test_split function
from sklearn import model_selection

# Split dataset into training set and test set
# 70% training and 30% test
X_train, X_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.3,random_state=0)
#-----------Model Generation ----------#
#Import linear svm model
from sklearn import svm #Import linear svm model
#creating the classifier
lc = svm.SVC(kernel="linear")
#training the classifier
lc.fit(X_train, y_train)
#Prediction
y_pred = lc.predict(X_test)
#----------Evaluating the model -------------#
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("classification_report\n",metrics.classification_report(y_test,y_pred))
