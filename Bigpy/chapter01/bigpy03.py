import pandas as pd

# uv pip install pandas / uv pip install openpyxl

user_list = pd.read_excel('sample.xlsx', sheet_name='Sheet1', engine='openpyxl')
print(user_list)