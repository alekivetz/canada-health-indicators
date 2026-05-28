import requests
import zipfile
import io
import pandas as pd
import os

zip_url = 'https://www150.statcan.gc.ca/n1/tbl/csv/13100096-eng.zip'
response = requests.get(zip_url)

with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    print(z.namelist())
    df = pd.read_csv(z.open('13100096.csv'))

print(df.shape)
print(df.head())
print(df.columns.tolist())

df.to_csv('bronze_health_indicators.csv', index=False)