import pandas as pd

# ✅ This is where you create the data
data = [{
    "Title": "General Manager",
    "Company": "Black Diamond",
    "Location": "Harare",
    "Expiry Date": "22 April 2025",
    "Description": ""
}]

# Create DataFrame from data
df = pd.DataFrame(data)

# Print the table
print(df)

# Optional: Save it to a CSV file
df.to_csv("example_na_data.csv", index=False)
