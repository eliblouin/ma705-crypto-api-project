import streamlit as st

st.title("Today's Cryptocurrency Prices 🪙")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

common_crypto_symbols = [
   'BTC', 'ETH', 'USDT', 'XRP', 'BNB', 'USDC', 'SOL', 'TRX', 'DOGE', 'HYPE', 'LEO', 'BCH', 'ADA', 'XMR', 'LINK', 'ZEC', 'CC', 'XLM', 'DAI', 'M', 'USD1', 'LTC', 'AVAX', 'HBAR', 'USDe', 'SUI', 'SHIB', 'PYUSD', 'TON', 'CRO', 'TAO', 'XAUt', 'USDG', 'WLFI', 'PAXG', 'MNT', 'SKY', 'UNI', 'DOT', 'PI', 'NEAR', 'OKB', 'ASTER', 'PEPE', 'RLUSD', 'AAVE', 'USDD', 'BGB', 'ICP', 'ETC', 'ONDO', 'DEXE', 'KCS', 'U', 'ALGO', 'ATOM', 'POL', 'ENA', 'RENDER', 'KAS', 'MORPHO', 'QNT', 'WLD', 'GT', 'STABLE', 'APT', 'ARB', 'FIL', 'JST', 'JUP', 'FLR', 'PENGU', 'VET', 'XDC', 'TRUMP', 'PUMP', 'NEXO', 'NIGHT', 'BONK', 'CHZ', 'SIREN', 'TUSD', 'CAKE', 'FET', 'ZRO', 'EDGE', 'VIRTUAL', 'DASH', 'EURC', 'AERO', 'SEI', 'FDUSD', 'VVV', 'STX', 'XTZ', 'H', 'ZBCN', '币安人生', 'LUNC', 'ETHFI', 'MON', 'INJ', 'SUN', 'SPX', 'CRV', 'LDO', 'IMX', 'GNO', 'DCR', 'TIA', 'NFT', 'BTT', 'BSV', 'CFX', 'FLOKI', 'KAIA', '2Z', 'JASMY', 'SYRUP', 'PYTH', 'KITE', 'GRT', 'OP', 'IOTA', 'AXS', 'ENS', 'XCN', 'SAND', 'COMP', 'RAVE', 'STRK', 'PENDLE', 'LIT', 'THETA', 'TEL', 'NEO', 'RAY', 'FARTCOIN', 'GENIUS', 'SFP', 'TWT', 'HNT', 'MANA', 'IP', 'VSN', 'WIF', 'XPL', 'RUNE', 'CVX', 'WAL', 'SKYAI', 'MX', 'JTO', 'GALA', 'BAT', 'AB', 'FF', 'TRAC', 'DEEP', 'CHIP', 'ZK', 'A', 'STG', 'XEC', 'AKT', 'B', 'GLM', 'BEAT', '1INCH', 'FLUID', 'RIVER', 'DYDX', 'SENT', 'S', 'EGLD', 'AR', 'EIGEN', 'ENJ', '0G', 'CFG', 'ATH', 'RSR', 'MELANIA', 'CHEEMS', 'WEMIX', 'AWE', 'SNX', 'GAS', 'ZEN', 'APE', 'LPT', 'COW', 'SAFE', 'KAITO', 'BEAM', 'YFI', 'FTT', 'ZRX', 'RVN', 'SPK'
]

crypto_symbol = st.selectbox(
    "Choose a cryptocurrency:",
    common_crypto_symbols,
)

import requests
import pandas as pd

def get_todays_crypto_prices(symbol):
  url = f"https://data.alpaca.markets/v1beta3/crypto/us/bars?symbols={symbol}%2FUSD&timeframe=1Min&limit=1000&sort=asc"
  headers = {"accept": "application/json"}
  response = requests.get(url, headers=headers)

  df = pd.DataFrame(response.json()['bars'][f'{symbol}/USD'])

  df['t'] = pd.to_datetime(df['t'])

  df = df.rename(columns= {
      't':'Time', 'o':'Open', 'h':'High', 'l':'Low', 'v':'Volume', 'n':'Count', 'c':'Close', 'vw':'VWAP'
  })

  # Reorder the columns more naturally
  df = df[['Time','Open','Close','High','Low','Volume','Count','VWAP']]

  # Round to two decimals, as USD should be rounded
  df[['Open','Close','High','Low','VWAP']] = df[['Open','Close','High','Low','VWAP']].round(2)

  return df

crypto_df = get_todays_crypto_prices(crypto_symbol)
st.dataframe(crypto_df)

crypto_quantity = st.selectbox(
    "Choose a quantity to graph:",
    crypto_df.columns[1:],
)

st.line_chart(data=crypto_df, x="Time", y=crypto_quantity)

