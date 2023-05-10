import pandas as pd

# read in the three CSV files as DataFrames
df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

# combine the three DataFrames into a single DataFrame
df = pd.concat([df1, df2, df3])

# filter out all rows that do not have "Pink Morsels" in the "product" field
df = df[df['product'] == 'pink morsel']

# calculate the sales for each row by multiplying the quantity and price fields
# print(df.shape) # execute the file
df['price'] = df['price'].apply(lambda x: float(x.replace('$', "")))
# print(df.dtypes)

df['sales'] = df['quantity'] * df['price']

# group the data by date and region, and sum the sales for each group
df = df.groupby(['date', 'region']).agg({'sales': 'sum'}).reset_index()

# output the resulting DataFrame to a CSV file
df.to_csv('sales_data.csv', index=False)