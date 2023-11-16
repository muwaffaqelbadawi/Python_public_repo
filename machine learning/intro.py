import pandas as pd
import quandl


df = quandl.get('WIKI/GOOGL', authtoken='wxF5A9xp2WcPEVmb8qCb')
print(df.head())