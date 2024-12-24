import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(url)

"""Function to plot the data"""


def plot_polly(model, independent_variable, dependent_variable, name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()


x = df['highway-mpg']
y = df['price']
"""Fitting the polynomial using the function polyfit, 
then using the function poly1d to display the polynomial function"""
f = np.polyfit(x, y, 3)
""" Polynomial of 3rd order"""
p = np.poly1d(f)
print(p)
plot_polly(p, x, y, 'highway-mpg')

"""Polynomial transform with multiple independent variables"""
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
pr = PolynomialFeatures(degree=2)
Z_pr = pr.fit_transform(Z)
print(Z.shape)
print(Z_pr.shape)

"""Pipeline
Data Pipelines simplify the steps of processing the data.
We create the pipeline, by creating a list of tuples 
including the name of the model or estimator and its corresponding constructor"""
Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)),
         ('model', LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(Z, y)
ypipe = pipe.predict(Z)
print(ypipe[0:4])