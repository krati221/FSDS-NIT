import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv(r'cluster/Investment.csv')
data.info()
data.isna().any

x = data.iloc[:,:-1]
y = data.iloc[:,4]
x = pd.get_dummies(x,dtype = int)
x.columns

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 , random_state = 0)
regressor = LinearRegression()
regressor.fit(x_train,y_train)
y_pred = regressor.predict(x_test)
 
bais = regressor.score(x_train,y_train)
variance = regressor.score(x_test,y_test)
m = regressor.coef_
c = regressor.intercept_
x = np.append(arr=np.full((50,1),42467).astype(int),values = x , axis = 1)

import statsmodels.api as sm 
x_opt = x[:,[0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog = y , exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1,2,3,5]]
regressor_ols = sm.OLS(endog = y , exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1,2,3]]
regressor_ols = sm.OLS(endog = y , exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1,3]]
regressor_ols = sm.OLS(endog = y , exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1]]
regressor_ols = sm.OLS(endog = y , exog = x_opt).fit()
regressor_ols.summary()
print(x_opt)

bais = regressor.score(x_train,y_train)
print(bais)

variance = regressor.score(x_test,y_test)
print(variance)


















