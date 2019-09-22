import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load data
import csv
import numpy as np
import pandas as pd
import datetime 
import time
from datetime import date, timedelta, datetime, tzinfo
import datetime as dt


# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)

magic_norm = pd.read_csv("test.csv", sep=',')
xx = magic_norm.iloc[:, 0:9]  # independent columns
xx.columns = [
    'datetime', 'season', 'holiday', 'workingday', 'weather', 'temp', 'atemp', 'humidity', 'windspeed']
yy = []
yy = magic_norm.iloc[:, :1]
#print(yy)  # target column
print("get Date Time Column")
print(type(yy))




print("************Format Date Time GO ************")
td=  pd.to_datetime(yy['datetime'], format="%Y-%m-%d %H:%M:%S")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
type(td)
print(td)
print("************Format Date Time Done ************")



for i in range(len(yy)):
   timestamp = datetime.timestamp(td[i])
   print("timestamp =", timestamp)
