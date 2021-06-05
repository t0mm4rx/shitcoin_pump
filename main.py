import ccxt
from dotenv import load_dotenv
import os

take_profits = [
    5,
    10,
    20,
    40,
    50
]

load_dotenv()

binance = ccxt.binance({
    'apiKey': os.getenv("BINANCE_KEY"),
    'secret': os.getenv("BINANCE_SECRET"),
})

balance = binance.fetch_balance()["BTC"]["free"] * 0.95

print(f"Will trade with {balance} available BTC.")
token = input("Enter the token name: ")
ticker = f"{token}/BTC"

print(f"Getting {ticker} price...")
price = binance.fetch_ticker(ticker)["last"]
print(f"Current price: {price}BTC")

qty_to_buy = binance.amount_to_precision(ticker, balance / price)
print(f"Buying market {token}/BTC (qty: {qty_to_buy})...")
binance.create_market_buy_order(ticker, qty_to_buy)

print(f"Getting amount of {token}...")
balance_token = binance.fetch_balance()[token]["free"]
print(f"Balance: {balance_token}{token}")

selling_amount = balance_token / len(take_profits)
selling_amount = binance.price_to_precision(ticker, selling_amount)

print(f"Will sell {selling_amount}{token} in {len(take_profits)} levels")

for take_profit in take_profits:
    print(f"Creating take profit at {take_profit}%...")
    binance.create_limit_sell_order(ticker, selling_amount, price * (1 + take_profit / 100))