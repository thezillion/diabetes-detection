import numpy as np
import pandas as pd
from sklearn import svm
import pickle

class Model(object):
    
    def __init__(self,filename):
        self.filename=filename

    def loadfile(self):
        filename='balanced.csv'
        names=['sno','preg','glu','bp','skin','insulin','bmi','pedigree','age','class']
        ds=pd.read_csv(filename,names=names)
        a=np.array([ds['glu'],ds['bp'],ds['insulin'],ds['bmi']])
        b=np.array(ds['class'])
        a=a.reshape(536,4)
        clt=svm.LinearSVC()
        pickle.dump(clt.fit(a,b),"model.txt")
    
         
