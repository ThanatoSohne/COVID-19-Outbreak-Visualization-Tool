

##############_____This is where we deviated a bit______#######################
#
#
#x = filtered_data.Confirmed.values.reshape(-1,1)
#y1 = filtered_data.Deaths.values.reshape(-1,1)
#
#train_x, test_x, train_y1, test_y1 = train_test_split (x, y1, test_size = 0.25, random_state = 1)
#linear_model = LinearRegression()
#linear_model.fit(train_x, train_y1)
#
#intercept = linear_model.intercept_
#coeff = linear_model.coef_
#
#test_prediction = linear_model.predict(test_x)
#
#df_model = pd.DataFrame({'Actual':test_y1.flatten(), 
#                        'Predicted':test_prediction.flatten()})
#
#################_____We'vw got this!!!!!!!!!!!!!!______#######################
 

