library(readr)
library(writexl)

# List the CSV files to combine
csv_files <- c("HB.csv","H.csv","B.csv")

# Create an empty list to store the data
data_frames <- list()

# Read each CSV file and store the data in the list
for (csv_file in csv_files) {
  data_frames[[csv_file]] <- read.csv(csv_file)
}

# Create the output Excel file
output_file <- "NETWORK.xlsx"

# Write the data list as separate sheets in the Excel file
write_xlsx(data_frames, path = output_file)

# Print a message indicating the combining is complete
cat("Excel file created:", output_file, "\n")

