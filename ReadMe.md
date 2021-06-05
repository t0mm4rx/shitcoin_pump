# Shitcoin pump

This script will:
- create a market buy orders
- place sell limit orders at given take_profits levels (in percentage)

For example:
```python
# In main.py
take_profits = [
    5,
    10,
    15
]
```
Will create 3 sell orders, 5%, 10%, and 15% above the current price.

The selling quantity will be equaly distributed for all levels. If you have 4 levels, each level will sell 25% of the position relative to the open quantity.



Create a .env file with your binance API keys.

```sh
BINANCE_KEY={{API_KEY}}
BINANCE_SECRET={{API_SECRET}}
```

Will trade in spot, with all BTC available.