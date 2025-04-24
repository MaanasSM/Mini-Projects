import pandas as pd

# Load Excel file
file_path = "participants.xlsx"  # Change to your file name
df = pd.read_excel(file_path)

# Extract phone numbers column
phone_numbers = df.iloc[:, 0].astype(str).tolist()  # Convert to string list

print("Extracted Phone Numbers:", phone_numbers)
