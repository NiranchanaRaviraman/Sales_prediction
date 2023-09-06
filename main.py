import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error,r2_score
print("CHECKING ALL INFOS")
sales=pd.read_csv("advertising.csv")
sales.head(10);
print(sales)

print();
print("CHECKING NULL VALUES");

print("Check for null values");
print(sales.info());

print("DROPPING ITEMS");

str_sales=sales.drop(['Radio','Newspaper'],axis=1)
print(str_sales)


print(str_sales.info())





