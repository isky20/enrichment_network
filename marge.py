import pandas as pd
import glob
import sys

# Specify the directory containing the CSV files
csv_files_path = '*all.csv'

# Use glob to get a list of all CSV files in the directory
csv_files = glob.glob(csv_files_path)

# Initialize an empty list to hold dataframes
dataframes = []

# Read each CSV file into a DataFrame and append it to the list
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Assuming you want to merge on a column named 'query'
# Use the first dataframe as the base and merge iteratively
merged_df = dataframes[0]
for df in dataframes[1:]:
    merged_df = pd.merge(merged_df, df, on='query term', how='outer')

# Display the combined DataFrame
merged_df.to_csv( sys.argv[1], index=False)


