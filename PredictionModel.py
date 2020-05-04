import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import svm
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
from scipy.optimize import curve_fit
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from scipy.optimize import curve_fit
import math
import datetime


# df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv')

# newAgain = pd.DataFrame(columns= ['Date','Country/Region','Confirmed', 'Recovered','Deaths'])

# rose = []
# test = list(df['Country/Region'].unique())

# for i in test:
    # niles = df.groupby('Country/Region').get_group(i)
    # rose.append(niles)
# for r in rose:
    # hold=[]
    # timeD = r['Date'].tolist()
    # for t in timeD:
        # delt = datetime.datetime.strptime(t, "%Y-%m-%d").strftime("%m%d%Y")
        # hold.append(delt)
    # r['date'] = hold
    # newAgain = pd.concat([newAgain, r])

# newAgain = newAgain.drop(columns = 'Date').astype({'date':'float64'})
# newAgain = newAgain.reindex(columns = ['date','Country/Region','Confirmed', 'Recovered','Deaths'])


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
print(newAgain)




filtered_data = df[newAgain["Country/Region"] =='US']
print(filtered_data)

x = filtered_data.Date.values.reshape(-1,1)
y1 = filtered_data.Confirmed.values.reshape(-1,1)



# To Predict Confirmed Cases (x, y1):
train_x, test_x, train_y1, test_y1 = train_test_split (x, y1, test_size = 0.25, random_state = 1)
train_x.shape
test_x.shape
train_y1.shape
test_y1.shape
linear_model = LinearRegression()
linear_model
linear_model.fit(train_x, train_y1)
test_prediction = linear_model.predict(test_x)
print(linear_model.coef_)
df_model = pd.DataFrame({'features': x.columns, 'coeff': linear_model.coef_})
df_model = df_model.sort_values(by = ['coeff'])
df_model
df_model.plot(x = 'features', y1 = 'coeff', kind = 'bar', figsize = (15, 10))
plt.show();
fdf = pd.concat([test_x, test_y1], 1)
fdf['Predicted'] = np.round(test_prediction, 1)
fdf['Prediction_Error_Confirmed'] = fdf['Confirmed'] - fdf['Predicted']  
fdf
print(fdf)

filtered_data.plot(x = 'Date', y = 'Confirmed', style = 'o')
