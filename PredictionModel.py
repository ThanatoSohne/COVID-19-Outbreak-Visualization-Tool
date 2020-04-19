

import numpy as np
import panda as pd
import sklearn
import seaborn as sns
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


train_x, test_x, train_y, test_y = train_test_split (x, y, test_size = 0.25, random_state = 1)
train_x.shape
test_x.shape
train_y.shape
test_y.shape

linear_model = LinearRegression()
linear_model
linear_model.fit(train_x, train_y)

test_prediction = linear_model.predict(test_x)
print(linear_model.coef_)
df_model = pd.DataFrame({'features': x.columns, 'coeff': linear_model.coef_})
df_model = df_model.sort_values(by = ['coeff'])
df_model

df_model.plot(x = 'features', y = 'coeff', kind = 'bar', figsize = (15, 10))
plt.show();

fdf = pd.concat([test_x, test_y], 1)
fdf['Predicted'] = np.round(predict_test, 1)

fdf['Prediction_Error'] = fdf[''] - fdf['Predicted']  
# Add something for fdf[''] - maybe fdf['Death']
fdf
