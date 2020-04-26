
# Team 10
# Prediction Model

import numpy as np
import panda as pd
import sklearn
import seaborn as sns
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
from scipy.optimize import curve_fit
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from scipy.optimize import curve_fit


data = pd.read_csv (r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
df = pd.DataFrame(data, columns= ['Date','Country','Confirmed', 'Recovered','Deaths'])

filtered_data = df[df.Country =='US']
print(filtered_data)

x = filtered_data.Date
y1 = filtered_data.Confirmed
y2 = filtered_data.Deaths
y3 = filtered_data.Recovered

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

# To Predict Deaths (x, y2):
train_x, test_x, train_y2, test_y2 = train_test_split (x, y2, test_size = 0.25, random_state = 1)
train_x.shape
test_x.shape
train_y2.shape
test_y2.shape
linear_model = LinearRegression()
linear_model
linear_model.fit(train_x, train_y2)
test_prediction = linear_model.predict(test_x)
print(linear_model.coef_)
df_model = pd.DataFrame({'features': x.columns, 'coeff': linear_model.coef_})
df_model = df_model.sort_values(by = ['coeff'])
df_model
df_model.plot(x = 'features', y2 = 'coeff', kind = 'bar', figsize = (15, 10))
plt.show();
fdf = pd.concat([test_x, test_y2], 1)
fdf['Predicted'] = np.round(test_prediction, 1)
fdf['Prediction_Error_Deaths'] = fdf['Deaths'] - fdf['Predicted']  
fdf

# To Predict Recovered Cases (x, y3):
train_x, test_x, train_y3, test_y3 = train_test_split (x, y3, test_size = 0.25, random_state = 1)
train_x.shape
test_x.shape
train_y3.shape
test_y3.shape
linear_model = LinearRegression()
linear_model
linear_model.fit(train_x, train_y3)
test_prediction = linear_model.predict(test_x)
print(linear_model.coef_)
df_model = pd.DataFrame({'features': x.columns, 'coeff': linear_model.coef_})
df_model = df_model.sort_values(by = ['coeff'])
df_model
df_model.plot(x = 'features', y3 = 'coeff', kind = 'bar', figsize = (15, 10))
plt.show();
fdf = pd.concat([test_x, test_y3], 1)
fdf['Predicted'] = np.round(test_prediction, 1)
fdf['Prediction_Error_Recovered'] = fdf['Recovered'] - fdf['Predicted']  
fdf