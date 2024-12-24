import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(url)
print(df.head())
""" 1) Linear Regression and Multiple Linear Regression """
lm = LinearRegression()
X = df[["highway-mpg"]]
Y = df["price"]
lm.fit(X, Y)
Yhat = lm.predict(X)
print(Yhat[0:5])
print("The intercept is:", lm.intercept_)
print("The slope is:", lm.coef_)

lm1 = LinearRegression()
X1 = df[['engine-size']]
Y1 = df['price']
lm1.fit(X1, Y1)
Yhat1 = lm1.predict(X1)
print("Engine size as the independent var and price as the dependent var ")
print("The intercept is:", lm1.intercept_)
print("The slope is:", lm1.coef_)

""" Multiple linear Regression """
lm2 = LinearRegression()
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm2.fit(Z, df['price'])
print("MLR with Horsepower, Curb-Weight, Engine Size and highway-mpg as predictor variables and price as the target variable")
print("The intercept is:", lm2.intercept_)
print("Coefficients")
print(lm2.coef_)
Y_hat = lm2.predict(Z)
"""Evaluation of MLR using Distribution Plot"""
plt.figure(figsize=(6, 4))
ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values", ax=ax1)
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')
plt.show()
plt.close()
""" Create and train a Multiple Linear Regression model "lm3" where the response variable is price, and the 
predictor variables are 'normalized-losses' and 'highway-mpg'."""
lm3 = LinearRegression()
Z1 = df[['normalized-losses', 'highway-mpg']]
lm3.fit(Z1, df['price'])
print("response variable is price, and the predictor variables are 'normalized-losses' and 'highway-mpg'")
print("Coefficients")
print(lm3.coef_)

""" 2) Model Evaluation using Visualization """

"""Let's visualize highway-mpg as potential predictor variable of price"""
plt.figure(figsize=(6, 4))
sns.regplot(x='highway-mpg', y='price', data=df)
plt.ylim(0,)
plt.title("Highway-mpg as potential predictor variable of Price")
plt.show()

"""Let's visualize peak-rpm as potential predictor variable of price"""
plt.figure(figsize=(8, 6))
sns.regplot(x='peak-rpm', y='price', data=df)
plt.ylim(0,)
plt.title("peak-rpm as potential predictor variable of Price")
plt.show()

print("Verifying the correlation")
print(df[['highway-mpg', 'peak-rpm', 'price']].corr())

"""Residual Plot"""
plt.figure(figsize=(6,4))
sns.residplot(df['highway-mpg'],df['price'])
plt.title("Residual Plot")
plt.show()
"""From this residual plot we see that the residuals are not randomly spread around the x-axis, 
which leads us to believe that maybe a non-linear model is more appropriate for this data."""
