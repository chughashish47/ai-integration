import pandas as pd
import sqlite3
import glob
import os

# # Merge several CSV files

# csv_files = os.path.join('*.csv')
# f_list = glob.glob(csv_files)
# df = pd.concat(map(pd.read_csv, f_list), ignore_index=True)
# print(df.shape)
# df.to_csv("new.csv", index=False)

# Create a connection to the SQLite database
# You don't need to create the database manually. If the database doesn't exist, sqlite3 will create it automatically when a connection is made.
conn = sqlite3.connect('./db/product.db')
df = pd.read_csv('sample_data.csv')

# # Write the data to a SQLite table
df.to_sql('products', conn, if_exists='replace', index=True)




# df = pd.concat([df1, df2], axis=1)
# df.to_csv("newpro.csv", index = False)

# print(df1.shape)
# print(df2.shape)
# print(df.shape)

# Close the connection
# conn.close()  