import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load data
import csv
import numpy as np
import pandas as pd
from datetime import datetime


# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)


date_column = ("datetime")
f = open("test.csv","r")
csv_reader = csv.reader(f)

headers = None
results = []
for data in csv_reader:
    if not headers:
        headers = []
        print("^^^^^^^^&&&&&&&&&&&&&&&&&&7^^^^^")
        for i, col in enumerate(data):
           print(col)

           if col in date_column:
            headers.append(i)


    else:

        results.append(([data[i] for i in headers]))



print("^^^^^^^^^^^^^")
# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)
print(now)

lengthOfResults= len(results)
print(lengthOfResults)


