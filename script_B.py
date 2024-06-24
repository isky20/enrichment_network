import pandas as pd
import re
import sys
import numpy as np

# Check if the filename and column range are provided as arguments
if len(sys.argv) != 3:
    print("Usage: python3 script.py <filename> <start_index>")
    sys.exit(1)

filename = sys.argv[1]
start_index = int(sys.argv[2])


# Load the CSV file
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print("File not found:", filename)
    sys.exit(1)

# Replace zeros with NaN
df.replace(0, np.nan, inplace=True)

df.dropna(inplace=True)
#df.to_csv(filename.replace("b.csv","")+"genes.csv", index=False)
columns_to_drop = [col for col in df.columns if col.startswith('Cen')]
df.drop(columns=columns_to_drop, inplace=True)

# Define the extract_number function
def extract_number(string):
    # Use regex to find the number in the string starting with "Br", "Cen", or "Bet"
    match = re.search(r'(?:Br|Cen|Bet)(-?\d+)', string)
    if match:
        number = int(match.group(1))
        return number
    else:
        return None

# Select columns within the specified range
selected_columns = df.iloc[:, start_index:]
print(selected_columns)
# Create a DataFrame to store conditions
conditions = pd.DataFrame()

# Apply the condition for each selected column
for column in selected_columns.columns:
    conditions[column] = df[column] > extract_number(column) *2

# Use boolean indexing to select rows where all conditions are True
selected_rows_all = df[conditions.all(axis=1)]
#selected_rows_any = df[conditions.any(axis=1)]

# Do whatever you want with selected_rows_all and selected_rows_any
# For example, print them
selected_rows_all.to_csv(filename.replace("b.csv","")+"all.csv", index=False)
#selected_rows_any.to_csv(filename.replace("b.csv","")+"any.csv", index=False)

