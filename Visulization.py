import pandas as pd
import matplotlib.pyplot as plt

print("The data")
sales = pd.read_csv("advertising.csv")

print(sales.head())


tv_data = sales['TV'].sum()
newspaper_data = sales['Newspaper'].sum()
radio_data = sales['Radio'].sum()
sales_data = sales['Sales'].sum()





plt.figure(figsize=(10, 6))
channels = ['TV', 'Newspaper', 'Radio', 'Sales']
data = [tv_data, newspaper_data, radio_data, sales_data]
plt.bar(channels, data, color=['#27005D', '#9400FF', '#AED2FF', '#E4F1FF'])
plt.xlabel("Channels")
plt.ylabel("Total")
plt.title("Tv, Newspaper, Radio, and Sales")
plt.show()


