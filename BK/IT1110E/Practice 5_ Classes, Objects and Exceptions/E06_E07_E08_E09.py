import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

class DataPreprocessing():
    def __init__(self):
        # Auto initialize necessary attributes of the object
        self.dataframe = None
        self.X = None
        self.y = None
        
    def read_from_csv(self):
        # Read data from .csv file into the dataframe and display the first 5 rows
        df = pd.read_csv('/home/s1rjam3s/Documents/Study/IT1110E/Practice 5: Classes, Objects and Exceptions/real_estate.csv', index_col='No')
        self.dataframe = df
    
    def set_attributes_and_output(self):
        # Set X and y to data attributes and output from the dataframe
        self.y = self.dataframe.pop("Y house price of unit area").to_numpy()
        self.X = self.dataframe.to_numpy()

    def final_train_test_data(self, attributes_list=[0,1,2,3,4,5], test_size=0.2) -> tuple:
        # Split the data X and output y into training data and testing data
        # Output: a tuple (X_train, X_test, y_train, y_test), using train_test_split with random_state=42
        return train_test_split(self.X[:, attributes_list], self.y, random_state=42, test_size=test_size)

class BaseClassRegressionAnalysis():
    def __init__(self):
        # Initialize a regressor, which will handle the LinearRegression model 
        self.regressor = LinearRegression()
    
    def fit(self, X, y):
        # The regressor learn from the training data with input X and output y
        self.regressor.fit(X, y)
        
    def predict(self, X):
        # The regressor predict the result with input X (after being trained)
        # The output has the same size as output y
        return self.regressor.predict(X)
    
    def mean_square_error(self, y_real, y_predict):
        # Compare the 2 output vectors: real output and prediction, using mean square error
        return sum([x**2 for x in [a - b for a, b in zip(y_predict, y_real)]])/len(y_real)



class PolynomialRegressionAnalysis(BaseClassRegressionAnalysis):
    def __init__(self, degree):
        super().__init__()
        self.degree = degree
    
    def __poly_transform(self, X):
        poly = PolynomialFeatures(degree=self.degree)
        Xt = poly.fit_transform(X)
        return Xt
    
    def fit(self, X, y, degree=2):
        Xt = self.__poly_transform(X)
        super().fit(Xt, y)
        
    def predict(self, X):
        Xt = self.__poly_transform(X)
        return super().predict(Xt)

dp = DataPreprocessing()
dp.read_from_csv()
dp.set_attributes_and_output()

X_train, X_test, y_train, y_test = dp.final_train_test_data(attributes_list=[2,4,5], test_size=0.2)

# Step 1: Initialize a polynomial regressor with degree 2 (a model) to learn from data
pr = PolynomialRegressionAnalysis(2)

# Step 2: The regressor will learn from the input and output of training data
pr.fit(X_train, y_train)

# Step 3: After learning from training data, the model will make a prediction
y_pred = pr.predict(X_test)

# Step 4: Comparision and visualization
print('First 10 instances prediction (rounded to 1 decimal place):     ', np.array([round(i, 1) for i in y_pred[:10]]))
print('Real output of first 10 instances (rounded to 1 decimal place): ', y_test[:10])
print('Mean square error (rounded to 1 decimal place):', round(pr.mean_square_error(y_test, y_pred),1))
