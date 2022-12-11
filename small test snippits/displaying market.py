from GUT import COLOR
import os
os.system("")
Fore = COLOR.Fore
Back = COLOR.Back

# Define a function to display the trading market
def display_market(prices):
    # Use ASCII characters to draw the market
    market_string = "+" + "-" * 20 + "+"
    print(Fore.GREEN() + market_string + Fore.RESET())

    # Display the prices for each item in the market
    for item, price in prices.items():
        print(Fore.YELLOW() + item + Fore.RESET() + ": " + Fore.MAGENTA() + str(price) + Fore.RESET())

    # Use ASCII characters to draw the bottom of the market
    print(Fore.GREEN() + market_string + Fore.RESET())

# Create a dictionary of prices for different items in the market
prices = {"Water": 10, "Food": 20, "Fuel": 30, "Ore": 40}

# Display the market
display_market(prices)
click = input('')
