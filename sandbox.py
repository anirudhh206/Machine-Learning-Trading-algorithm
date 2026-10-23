import pandas as pd
import numpy as np

dates = pd.date_range(start='2024-01-01', periods=10, freq='B')
print(dates)

rng = np.random.default_rng(42)
returns = rng.normal(loc = 0.0005, scale=0.01, size=10)  # daily returns

prices = 100 * np.cumprod(1 + returns)
priceseries = pd.Series(prices, index=dates, name='close')
print(priceseries)

ma_3 = priceseries.rolling(window=3).mean()
print(ma_3)

log_returns = np.log(priceseries / priceseries.shift(1))
print(log_returns)

df = pd.DataFrame({
    'open': prices * np.random.uniform(0.99, 1.00, 10),
    'high': prices * np.random.uniform(1.00, 1.02, 10),
    'low': prices * np.random.uniform(0.98, 1.00, 10),
    'close': prices,
    'volume': np.random.randint(1000, 10000, size=10)
}, index=dates)
print(df)

weekly = df.resample('W').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
})
print(weekly)
