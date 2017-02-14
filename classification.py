import pandas as pd
from sklearn import svm
import numpy as np
import pickle
import model

class Classify(object):

    def __init__(self,filename):
        self.filename=filename
        pickle.load("model.txt")

    def predict(self,glucose,blood_pressure,insulin,bmi):
        names=['sno','preg','glu','bp','skin','insulin','bmi','pedigree','age','class']
        ds=pd.read_csv(filename,names=names)
        a=np.array([ds['glu'],ds['bp'],ds['insulin'],ds['bmi']])
        b=np.array(ds['class'])
        a=a.reshape(536,4)
        clt=svm.LinearSVC()
        clt.fit(a,b)
        return (clt.predict([glucose,blood_pressure,insulin,bmi]))

if __name__=='__main__':
    obj=Classify('data.csv')
    glucose,blood_pressure,insulin,bmi=input().split()
    obj.predict()
