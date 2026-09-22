import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_379644.csv",skiprows=4)
print(data.head())
data.plot(x="Country Name",y = "2023",kind="bar",figsize=(12,6))
plt.title("Population Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Population")
plt.show()