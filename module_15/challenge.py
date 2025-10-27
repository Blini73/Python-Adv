import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("weather_tokyo_data.csv")


df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


df["date"] = pd.to_datetime(df["year"].astype(str) + "/" + df["day"], errors="coerce")


df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")


average_temp = round(df["temperature"].mean(), 2)
print(f"Average Temperature for the entire dataset: {average_temp} °C")


df["month"] = df["date"].dt.month
monthly_avg_temp = df.groupby("month")["temperature"].mean().round(2)
print("\nAverage Monthly Temperatures (°C):\n", monthly_avg_temp)


plt.figure(figsize=(10,6))
plt.bar(monthly_avg_temp.index, monthly_avg_temp.values, color="skyblue", edgecolor="black")
plt.title("Average Monthly Temperature in Tokyo")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


hottest_day = df.loc[df["temperature"].idxmax(), ["date", "temperature"]]
coldest_day = df.loc[df["temperature"].idxmin(), ["date", "temperature"]]
print(f"\nHottest Day: {hottest_day['date'].date()} - {hottest_day['temperature']} °C")
print(f"Coldest Day: {coldest_day['date'].date()} - {coldest_day['temperature']} °C")


plt.figure(figsize=(12,6))
plt.plot(df["date"], df["temperature"], linewidth=1.5, color="orange")
plt.title("Temperature Changes Over Time in Tokyo")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()



def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["month"].apply(get_season)
seasonal_avg_temp = df.groupby("season")["temperature"].mean().round(2)
print("\nSeasonal Average Temperatures (°C):\n", seasonal_avg_temp)


plt.figure(figsize=(8,5))
plt.bar(seasonal_avg_temp.index, seasonal_avg_temp.values, color="salmon", edgecolor="black")
plt.title("Seasonal Average Temperature in Tokyo")
plt.xlabel("Season")
plt.ylabel("Average Temperature (°C)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()