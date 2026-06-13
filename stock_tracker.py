# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

num_stocks = int(input("How many stocks do you own? "))

for i in range(num_stocks):
    stock_name = input("\nEnter Stock Name (AAPL/TSLA/GOOG/MSFT): ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment in", stock_name, "=", investment)

    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_investment)

# Save result to file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")