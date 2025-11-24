
stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 300}
portfolio = {}
total_investment = 0

print("Enter your stock details (type 'done' to finish):")

while True:
    name = input("Stock symbol: ").upper()
    if name == "DONE":
        break
    if name not in stocks:
        print("Stock not found in list! Available:", list(stocks.keys()))
        continue
    qty = int(input("Quantity: "))
    investment = stocks[name] * qty
    portfolio[name] = investment
    total_investment += investment

print("\n Portfolio Summary:")
for stock, value in portfolio.items():
    print(f"{stock}: ${value}")

print(f"\n Total Investment: ${total_investment}")
