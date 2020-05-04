# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import svm
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"
from scipy.optimize import curve_fit
import math
import datetime
import matplotlib.animation as anim



df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv')
col_name = ['Date', 'Country/Region', 'Province/State', 'Lat', 'Long', 'Confirmed', 'Recovered', 'Deaths', 'date']
newAgain = pd.DataFrame(columns = col_name)

rose = []
test = list(df['Country/Region'].unique())

for i in test:
    niles = df.groupby('Country/Region').get_group(i)
    rose.append(niles)
for r in rose:
    hold=[]
    timeD = r['Date'].tolist()
    for t in timeD:
        delt = datetime.datetime.strptime(t, "%Y-%m-%d").strftime("%m%d%Y")
        hold.append(delt)
    r['date'] = hold
    newAgain = pd.concat([newAgain, r])

newAgain = newAgain.drop(columns = 'Date').astype({'date':'float64'})
newAgain = newAgain.reindex(columns = ['date', 'Country/Region', 'Province/State', 'Lat', 'Long', 'Confirmed', 'Recovered', 'Deaths'])

filtered_data = newAgain[newAgain["Country/Region"] =='US']
US = filtered_data.drop(columns = ['Province/State','Lat', 'Long']) 


x = filtered_data.Confirmed.values.reshape(-1,1)
y = filtered_data.Deaths.values.reshape(-1,1)

# To Predict Number of Deaths from Confirmed Cases:
train_x, test_x, train_y, test_y = train_test_split (x, y, test_size = 0.25, random_state = 1)
linear_model = LinearRegression()
linear_model.fit(train_x, train_y)

intercept = linear_model.intercept_
coeff = linear_model.coef_

test_prediction = linear_model.predict(test_x)

df_model = pd.DataFrame({'Actual':test_y.flatten(), 
                        'Predicted':test_prediction.flatten()})

df_DA = pd.DataFrame({'Actual Confirmed':x.flatten(),
                     'Actual Deaths':y.flatten(),})

df_DP = pd.DataFrame({'Predicted Confirmed':test_x.flatten(),
                     'Predicted Deaths':test_prediction.flatten()})

# df_model = df_model.sort_values(by = ['coeff'])
# df_model


plt.title("Prediction Model") 
plt.xlabel("Confirmed Cases") 
plt.ylabel("Deaths") 
plt.plot(x, y, label = 'Actual')
plt.plot(test_x, test_prediction, label = 'Predicted') 
plt.legend(loc = 'upper left')
plt.show()


# df_model.plot(x = 'Confirmed', y = 'coeff', kind = 'bar', figsize = (15, 10))
# fdf = pd.concat([test_x, test_y1], 1)
# fdf['Predicted'] = np.round(test_prediction, 1)
# fdf['Prediction_Error_Confirmed'] = fdf['Deaths'] - fdf['Predicted'] 
# fdf

df_DA.to_csv('Death_Actual.csv', index = True, header = True)
df_DP.to_csv('Death_Predict.csv', index = True, header = True)