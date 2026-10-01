#  Stock Portfolio Tracker

##  Project Description

Stock Portfolio Tracker is a beginner-friendly Python application that calculates the total investment value of stocks based on manually defined stock prices.

The user can view available stocks, add stocks with a desired quantity, and view their personal portfolio along with the total investment value.

##  Objective

The main objective of this project is to practice Python programming concepts such as:

* Dictionaries
* Lists
* Functions
* Loops
* Conditional statements
* User input
* Exception handling
* Basic arithmetic
* String formatting

##  Features

*  Display available stocks and their prices
*  Add multiple stocks to the portfolio
*  Enter the quantity of each stock
*  Calculate the value of each stock
*  Calculate the total portfolio investment
*  View the complete portfolio
*  Handle invalid stock names
*  Handle invalid quantity input
*  Menu-based interface

##  Python Concepts Used

### 1. Dictionary

A dictionary is used to store stock names and their prices.

stocks = {
    "AAPL": 1500,
    "MSFT": 2500,
    "TSLA": 3500,
    "INFO": 4500,
    "GOOGL": 5000,
    "TATA": 6000,
    "AMZN": 7000
}

### 2. Lists

A list is used to store the stocks added to the user's portfolio.

portfolio = []

Each portfolio entry contains:

Stock Name
Quantity
Price
Total Value

### 3. Functions

The program is divided into functions to make the code organized and easier to understand.

display_stocks()
add_stocks()
view_mystocks()

### 4. Loops

'for' loops are used to display stocks and process multiple stock entries.

A 'while' loop is used to keep the menu running until the user chooses Exit.

### 5. Exception Handling

'try-except' is used to handle invalid quantity input.

try:
    quantity = int(input("Enter quantity: "))
except ValueError:
    print("Invalid input.")

### 6. Basic Arithmetic

The investment value is calculated using:

Stock Value = Stock Price × Quantity

The values of all stocks are added together to calculate the total investment.

##  How the Program Works

When the program starts, it displays a welcome message and provides a menu.

1. Display Stocks
2. Add Stocks
3. View My Portfolio
4. Exit

### Option 1: Display Stocks

Displays all available stocks and their predefined prices.

### Option 2: Add Stocks

The user enters:

1. Number of stocks to add
2. Stock name
3. Quantity

The program then calculates:

Price × Quantity = Investment Value

The stock information is stored in the portfolio.

### Option 3: View My Portfolio

Displays the stocks added by the user, including:

* Stock name
* Price
* Quantity
* Total value

It also displays the total investment.

### Option 4: Exit

Terminates the program.

##  How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:
python --version

### 2. Clone the Repository

### 3. Open the Project Folder

cd CodeAlpha_StockPortfolioTracker

### 4. Run the Program

stockportfolio.py

##  Sample Output

==================================================
        Welcome to Stock Portfolio Tracker
==================================================

1. Display Stocks
2. Add Stocks
3. View My Portfolio
4. Exit

Enter your choice: 1

Available Stocks:
APPL: $1500
MSFT: $2500
TSLA: $3500
INFO: $4500
GOOLE: $5000
TATA: $6000
AMZN: $7000

Enter your choice: 2

Enter the number of stocks you want to add: 2

Enter the stock name: APPL
Enter the quantity of APPL you want to add: 2

Enter the stock name: TSLA
Enter the quantity of TSLA you want to add: 3

Enter your choice: 3

--------------------------------------------------
             Your Stock Portfolio:
--------------------------------------------------
Stock Name     Price          Quantity       Total Value
--------------------------------------------------
APPL           $1500          2              $3000
TSLA           $3500          3              $10500
--------------------------------------------------
Total value of your portfolio is: $13500

##  Future Improvements

The project can be extended with:

* Input validation for menu choices
* Preventing negative quantities
* Removing stocks from the portfolio
* Updating stock quantities
* Saving portfolio data to a CSV file
* Using real-time stock prices through an API
* Adding a graphical user interface
* Adding database support

##  Project Structure
CodeAlpha_StockPortfolioTracker
│
├── stockportfolio.py
├── README.md
└── .gitignore