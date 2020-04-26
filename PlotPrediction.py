
# Team 10
# Prediction Model

import pandas as pd
#import numpy as np
#import sklearn
#import seaborn as sns
#from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
from IPython.core.interactiveshell import InteractiveShell
from scipy.stats import linregress
InteractiveShell.ast_node_interactivity = "all"

data = pd.read_csv (r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
df = pd.DataFrame(data, columns= ['Date','Country','Confirmed', 'Recovered','Deaths'])

filtered_data = df[df.Country =='US']
print(filtered_data)

x = filtered_data.Date
y1 = filtered_data.Confirmed
y2 = filtered_data.Deaths
y3 = filtered_data.Recovered

stats1 = linregress(x, y1)
m1 = stats1.slope
b1 = stats1.intercept
regress_Confirmed = (m1 * x + b1) 
# Change the default figure size
plt.figure(figsize = (10, 10))
plt.title("Confirmed Cases Prediction")
plt.legend(loc = 'lower left')
# Add x and y lables, and set their font size
plt.xlabel("Date", fontsize=20)
plt.ylabel("Confirmed Cases", fontsize=20)
# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.plot(x, y1, color = "purple")
plt.plot(x, regress_Confirmed, color="red") 
plt.show()

stats2 = linregress(x, y2)
m2 = stats2.slope
b2 = stats2.intercept
regress_Deaths = (m2 * x + b2)
# Change the default figure size
plt.figure(figsize = (10, 10))
plt.title("Deaths Prediction")
plt.legend(loc = 'lower left')
# Add x and y lables, and set their font size
plt.xlabel("Date", fontsize=20)
plt.ylabel("Deaths", fontsize=20)
# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.plot(x, y2, color = "blue")
plt.plot(x, regress_Deaths, color="red") 
plt.show()

stats3 = linregress(x, y3)
m3 = stats3.slope
b3 = stats3.intercept
regress_Recovered = (m3 * x + b3)
# Change the default figure size
plt.figure(figsize = (10, 10))
plt.title("Recovered Cases Prediction")
plt.legend(loc = 'lower left')
# Add x and y lables, and set their font size
plt.xlabel("Date", fontsize=20)
plt.ylabel("Recovered Cases", fontsize=20)
# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.plot(x, y3, color = "green")
plt.plot(x, regress_Recovered, color="red")
plt.show()


# Change the default figure size
plt.figure(figsize = (10, 10))
plt.title("Case Predictions")
plt.legend(loc = 'lower left')
# Add x and y lables, and set their font size
plt.xlabel("Date", fontsize=20)
plt.ylabel("Case Predictions", fontsize=20)
# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.plot(x, regress_Confirmed, color="blue")
plt.plot(x, regress_Deaths, color = "red")
plt.plot(x, regress_Recovered, color="green")
plt.show()



