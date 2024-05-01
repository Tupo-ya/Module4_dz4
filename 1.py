import pandas as pd

data = pd.read_csv("Yacht_Motorboat Pricing Data - Sheet1.csv")

data[["Currency", "PriceValue"]] = data["Price"].str.extract(r"([A-Za-z]+)\s([\d.,]+)")

data["PriceValue"] = (
    data["PriceValue"].str.replace(".", "").str.replace(",", "").astype(float)
)

# print("Значения в столбах:")
# print(data[["PriceValue", "Currency"]].head())


currency_rates = {"EUR": 85.0, "CHF": 78.0}
data["PriceInRubles"] = data.apply(
    lambda row: row["PriceValue"] * currency_rates.get(row["Currency"], 1), axis=1
)

# print("Рублики:")
# print(data[["PriceInRubles"]].head())

data["PublishDay"] = pd.to_datetime(
    data["Advertisement Date"], dayfirst=True
).dt.dayofweek

#?                                                                              рабочих дней - 5
filtered_data = data[(data["Condition"].isin(["is new", "very good"])) & (data["PublishDay"] <= 5)]

print("Фильтрованные данные:")
print(filtered_data[["Condition", "PublishDay", "PriceInRubles"]].head())

average_price = filtered_data["PriceInRubles"].mean()
print("Средния стоимость:", average_price)
