# Shitcoin pump

## What is it

This script has been created to beat the average participant in organized shitcoin pumps.

It will market buy, then create limit sell orders at given price levels.

It's working on Binance but it's spot trading so you can change the exchange really easily.

It's working with BTC pairs, again it's easy to adapt.

## How to use?

You can define the percentage levels you want to sell in the take_profits array.
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



The script will wait for your input to run, so if you participate in a pump:

- Split your screen with your terminal and pump group side by side

- Before the token anouncement, run the script

  ```sh
  python3 main.py
  ```

- When the token is announced you just have to type the token name in the prompt and hit enter
- Enjoy being rich (I hope so)