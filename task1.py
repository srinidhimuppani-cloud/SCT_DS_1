import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_379644.csv",skiprows=4)
print(data.head())
# Select the top 10 countries by population
top10 = data.nlargest(10, "2023")

# Create the bar chart
plt.figure(figsize=(12, 6))

plt.bar(top10["Country Name"], top10["2023"])

plt.title("Top 10 Countries by Population in 2023")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()