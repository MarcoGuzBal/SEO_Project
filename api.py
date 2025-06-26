import requests
import os
import pandas as pd
import sqlalchemy as db

API_KEY=os.environ.get('EXCHANGERATE_API_KEY')

url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

response = requests.get(url).json()
engine = db.create_engine('sqlite:///data_base_name.db')

dataframe_name=pd.DataFrame.from_dict(response)

dataframe_name.to_sql('table_name', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))