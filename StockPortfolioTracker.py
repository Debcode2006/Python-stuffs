import csv
from datetime import datetime

# Predefined stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 370,
    "AMZN": 145,
}

def get_portfolio_input():
    """Get stock portfolio input from user"""
    portfolio = {}
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        
        if stock not in STOCK_PRICES:
            print(f"Stock {stock} not found in our database. Available stocks: {', '.join(STOCK_PRICES.keys())}")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity > 0:
                portfolio[stock] = quantity
            else:
                print("Please enter a positive quantity.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return portfolio

def calculate_portfolio_value(portfolio):
    """Calculate total value of the portfolio"""
    total_value = 0
    portfolio_details = []
    
    for stock, quantity in portfolio.items():
        stock_value = STOCK_PRICES[stock] * quantity
        total_value += stock_value
        portfolio_details.append({
            'stock': stock,
            'quantity': quantity,
            'price': STOCK_PRICES[stock],
            'value': stock_value
        })
    
    return total_value, portfolio_details

def save_to_csv(portfolio_details, total_value):
    """Save portfolio details to a CSV file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.csv"
    
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['stock', 'quantity', 'price', 'value'])
        writer.writeheader()
        writer.writerows(portfolio_details)
        
        # Add total value as the last row
        writer.writerow({
            'stock': 'TOTAL',
            'quantity': '',
            'price': '',
            'value': total_value
        })
    
    return filename

def main():
    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks:", ', '.join(STOCK_PRICES.keys()))
    
    # Get portfolio input from user
    portfolio = get_portfolio_input()
    
    if not portfolio:
        print("No stocks added to portfolio.")
        return
    
    # Calculate portfolio value
    total_value, portfolio_details = calculate_portfolio_value(portfolio)
    
    # Display results
    print("\nPortfolio Summary:")
    print("-" * 50)
    for detail in portfolio_details:
        print(f"{detail['stock']}: {detail['quantity']} shares @ ${detail['price']} = ${detail['value']}")
    print("-" * 50)
    print(f"Total Portfolio Value: ${total_value:,.2f}")
    
    # Ask if user wants to save results
    save = input("\nWould you like to save the results to a CSV file? (yes/no): ").lower()
    if save == 'yes':
        filename = save_to_csv(portfolio_details, total_value)
        print(f"Portfolio saved to {filename}")

if __name__ == "__main__":
    main()
