import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


print("MODEL PERFORMNCES")
data= pd.read_csv('advertising.csv')
X = data[['Radio']]
y = data['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mean = mean_squared_error(y_test, y_pred)
r_square = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mean}")
print(f"R-squared: {r_square}")

print("Visulization of them!!!")

plt.scatter(X_test, y_test, color='yellow', label='Actual')
plt.plot(X_test, y_pred, color='black', linewidth=2, label='Predicted')
plt.xlabel('Radio')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.title('Radio vs. Sales')
plt.show()
