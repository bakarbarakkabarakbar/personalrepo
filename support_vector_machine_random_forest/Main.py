from inspect import getfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import mean_absolute_error
import seaborn as sns
sns.set(style='ticks', rc={'figure.figsize':(3, 3)})
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        loadUi('GUI.ui', self)
        self.pushButton_2.clicked.connect(self.getFileName)
        self.pushButton.clicked.connect(self.klasifikasi) 

    def getFileName(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Single File', 'gab1' , '*.csv')
        self.lineEdit.setText(fileName)
        self.fileName = self.lineEdit.text()

    def klasifikasi(self):
        global X_train, y_train, X_test, y_test, scores

        df = pd.read_csv(self.lineEdit.text(), header=None)
        f,ax = plt.subplots(1,2,figsize=(10,10))
        X = df.iloc[:, 2:4].values
        y = df.iloc[:, -1].values
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=45)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.fit_transform(X_test)
        type(X_train), type(X_test)
        scores = pd.DataFrame(columns=['Model', 'Score'])


        #klasifikasi model SVM
        model = SVC(probability=True)
        model.fit(X_train, y_train)
        y_pred_svm = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred_svm)
        self.lineEdit_2.setText(str(accuracy * 100))
        scores = scores.append({'Model': 'SVC', 'Score': accuracy}, ignore_index=True)
        self.lineEdit_3.setText(str(mean_absolute_error(y_pred_svm, y_test)))
        cm_svm = confusion_matrix(y_test, y_pred_svm)
    

        #model Random forest
        model = GridSearchCV(estimator=RandomForestClassifier(), param_grid={'n_estimators': [50, 100, 200, 300], 'max_depth': [2, 3, 4, 5]}, cv=4)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        self.lineEdit_4.setText(str(accuracy * 100))
        scores = scores.append({'Model': 'Random Forest', 'Score': accuracy}, ignore_index=True)
        self.lineEdit_5.setText(str(mean_absolute_error(y_pred, y_test)))
        cm_rf = confusion_matrix(y_test, y_pred)

        f,ax=plt.subplots(2,1, figsize=(5,5)) 
        sns.heatmap(cm_svm, annot=True, fmt='g', ax=ax[0]);  #annot=True to annotate cells, ftm='g' to disable scientific notation
        sns.heatmap(cm_rf, annot=True, fmt='g', ax=ax[1]);  #annot=True to annotate cells, ftm='g' to disable scientific notation


        # labels, title and ticks
        ax[0].set_xlabel('Predicted labels');ax[0].set_ylabel('True labels'); 
        ax[0].set_title('Confusion Matrix SVM'); 
        ax[0].xaxis.set_ticklabels(['Kategori 1', 'Kategori 2']); ax[0].yaxis.set_ticklabels(['Kategori 1', 'Kategori 2']);

        ax[1].set_xlabel('Predicted labels');ax[1].set_ylabel('True labels'); 
        ax[1].set_title('Confusion Matrix RF'); 
        ax[1].xaxis.set_ticklabels(['Kategori 1', 'Kategori 2']); ax[1].yaxis.set_ticklabels(['Kategori 1', 'Kategori 2']);


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())


