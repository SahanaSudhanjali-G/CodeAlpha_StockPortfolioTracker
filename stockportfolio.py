stocks = {
    "AAPL"  :  1500,
    "MSFT"  :  2500,
    "TSLA"  :  3500,
    "INFO"  :  4500,
    "GOOGL" :  5000,
    "TATA"  :  6000,
    "AMZN"  :  7000,
}
print("="*50)
print(       "Welcome to Stock Portfolio Tracker")
print("="*50)
total = 0
portfolio = []
def display_stocks():
    print("Available Stocks:")
    for stock, price in stocks.items():
        print(f"{stock}: ${price}")

def add_stocks():
    global total
    number_of_stocks = int(input("Enter the number of stocks you want to add: "))
    for i in range(number_of_stocks):
        stock_name = input("Enter the stock name: ").upper()
        if stock_name in stocks:
            try:
                quantity = int(input(f"Enter the quantity of {stock_name} you want to add: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            price = stocks[stock_name]
            value = price * quantity
            total = total + value 
            portfolio.append((stock_name, quantity, price, value))
        else: 
            print(f"{stock_name} is not available in the stock list.")
        print(f"Total value of your portfolio is: ${total}")
def view_mystocks():
    print("\n" + "-"*50)
    print("             Your Stock Portfolio:")
    print("-"*50)
    print(f"{'Stock Name':<15}{'Price':<15}{'Quantity':<15}{'Total Value':<15}")
    for stock_name, quantity, price, value in portfolio:
        print(f"{stock_name:<15}${price:<14}{quantity:<15}${value:<14}")
    print("-"*50)
    print(f"Total value of your portfolio is: ${total}")


while True:
    print(" \n 1. Display Stocks")
    print(" 2. Add Stocks")
    print(" 3. View My Portfolio")
    print(" 4. Exit")

    choice = int(input("Enter your choice; "))

    if choice == 1:
        display_stocks()
    elif choice == 2:
        add_stocks()
    elif choice == 3:
        view_mystocks()
    elif choice == 4:
        print("Application Terminated Successfully")
        break
    else:
        print("Invalid choice. Please try again.")
        

