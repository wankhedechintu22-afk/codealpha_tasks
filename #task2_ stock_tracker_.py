# Hardcoded dictionary of stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "AMZN": 175, "MSFT": 400}

total_investment = 0
user_portfolio = {}

print("=== Stock Portfolio Tracker ===")
print("Available stocks: AAPL, TSLA, GOOGL, AMZN, MSFT\n")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter number of shares: "))
        price = stock_prices[stock]
        cost = price * quantity

        user_portfolio[stock] = quantity
        total_investment = total_investment + cost
        print("Added", quantity, "shares of", stock, "valuing $" + str(cost))
    else:
        print("Stock not found in market database!")

print("\n----------------------------------")
print("TOTAL INVESTMENT VALUE: $" + str(total_investment))
print("----------------------------------")

# Save summary to a txt file
file = open("portfolio_summary.txt", "w")
file.write("=== Portfolio Summary ===\n")
for stock, qty in user_portfolio.items():
    file.write(
        stock
        + ": "
        + str(qty)
        + " shares = $"
        + str(stock_prices[stock] * qty)
        + "\n"
    )
file.write("Total Investment: $" + str(total_investment) + "\n")
file.close()

print("Summary saved to portfolio_summary.txt")