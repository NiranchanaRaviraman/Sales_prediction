import pandas as pd
import matplotlib.pyplot as plt


sales_data = pd.read_csv("advertising.csv")


Radio = sales_data['Radio']
sales = sales_data['Sales']


plt.figure(figsize=(10, 6))
plt.scatter(Radio, sales, alpha=0.4)
plt.xlabel("Radio ")
plt.ylabel("Sales")
plt.title("Radio vs. TV ")


plt.show()
