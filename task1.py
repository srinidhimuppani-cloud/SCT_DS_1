
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read dataset skipping metadata rows
data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_379644.csv", skiprows=4)

# 2. Convert 2023 population column to numeric, ignoring errors
data["2023"] = pd.to_numeric(data["2023"], errors="coerce")

# 3. Filter out non-country regional aggregates
aggregates = [
    "World", "High income", "OECD members", "Post-demographic dividend", 
    "IDA & IBRD total", "Low & middle income", "Middle income", 
    "IBRD only", "East Asia & Pacific", "Late-demographic dividend", 
    "South Asia", "Lower middle income", "Africa Eastern and Southern",
    "Africa Western and Central", "Sub-Saharan Africa", "European Union",
    "Latin America & Caribbean", "Middle East & North Africa", "North America"
]

# Drop rows without population data and exclude aggregate groups
df_countries = data.dropna(subset=["2023"]).copy()
df_countries = df_countries[~df_countries["Country Name"].isin(aggregates)]

# 4. Get top 10 countries by 2023 population
top10 = df_countries.nlargest(10, "2023")

# 5. Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(top10["Country Name"], top10["2023"] / 1e8, color="skyblue", edgecolor="black")

plt.title("Top 10 Countries by Population (2023)", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Population (in Hundreds of Millions)", fontsize=12)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# 6. Save image and display
plt.savefig("population_bar_chart.png", dpi=300)
plt.show()