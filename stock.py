import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2900, 
    "AMZN": 3500,
    "MSFT": 320,
    "META": 470,
    "NFLX": 600,
    "INFY": 1425,
    "TCS": 3825,
    "RELIANCE": 2800,
    "HDFCBANK": 1640,
    "WIPRO": 450
}

def get_portfolio():
    portfolio = {}
    try:
        n = int(input(" How many different stocks would you like to enter? "))
    except ValueError:
        print(" Invalid input. Please enter a number.")
        return portfolio

    for i in range(n):
        print(f"\nStock {i+1}:")
        stock = input("🔸 Enter stock symbol (e.g., AAPL): ").upper()
        if stock not in stock_prices:
            print(f" {stock} is not in the available stock list. Skipping.")
            continue
        try:
            quantity = int(input(f"🔹 Enter quantity of {stock}: "))
            if quantity < 0:
                print(" Quantity can't be negative. Skipping.")
                continue
        except ValueError:
            print(" Invalid quantity. Skipping this stock.")
            continue
        portfolio[stock] = quantity
    return portfolio

def calculate_total(portfolio):
    total = 0
    for stock, qty in portfolio.items():
        total += stock_prices[stock] * qty
    return total

def save_to_file(portfolio, total, file_format='csv'):
    filename = f"portfolio_summary.{file_format}"

    if file_format == 'txt':
        with open(filename, "w") as file:
            for stock, qty in portfolio.items():
                file.write(f"{stock}: {qty} shares @ Rs {stock_prices[stock]} each\n")
            file.write(f"\nTotal Investment: Rs {total:,.2f}")
    elif file_format == 'csv':
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price per Unit", "Subtotal"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
            writer.writerow(["", "", "Total Investment", total])

    print(f"Portfolio saved to {filename}.")

def main():
    print(" Welcome to the Enhanced Stock Portfolio Tracker ")
    print("-" * 55)
    print("Available Stocks:")
    print(", ".join(stock_prices.keys()))
    print("-" * 55)

    portfolio = get_portfolio()

    if not portfolio:
        print("\n No valid stocks entered. Exiting.")
        return

    total_investment = calculate_total(portfolio)

    print("\n Portfolio Summary:")
    print("-" * 55)
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        subtotal = price * qty
        print(f"{stock:10s} | Qty: {qty:<3} | Rs {price:,.2f} each | Subtotal: Rs {subtotal:,.2f}")
    print("-" * 55)
    print(f" Total Investment: Rs {total_investment:,.2f}")

    save = input("\n Save this summary to file? (yes/no): ").lower()
    if save == "yes":
        file_type = input(" File format (txt/csv): ").lower()
        if file_type not in ['txt', 'csv']:
            print(" Invalid format. Defaulting to CSV.")
            file_type = 'csv'
        save_to_file(portfolio, total_investment, file_type)
    else:
        print(" Summary not saved.")

if __name__ == "__main__":
    main()
