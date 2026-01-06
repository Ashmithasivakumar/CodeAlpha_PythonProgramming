# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_value = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from available stocks.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = quantity

# Calculate total investment
print("\n📊 Portfolio Summary")
print("-" * 30)

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ₹{stock_prices[stock]} = ₹{value}")

print("-" * 30)
print(f"💰 Total Investment Value: ₹{total_value}")

# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-" * 30 + "\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares = ₹{value}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total Investment Value: ₹{total_value}")

    print("✅ Portfolio saved to portfolio.txt")
