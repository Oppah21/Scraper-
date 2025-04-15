import pandas as pd

# ✅ This is where you create the data
data = [{
    "Title": "N/A",
    "Company": "N/A",
    "Location": "N/A",
    "Expiry Date": "N/A",
    "Description": "N/A"
}]

# Create DataFrame from data
df = pd.DataFrame(data)

# Print the table
print(df)

# Optional: Save it to a CSV file
df.to_csv("example_na_data.csv", index=False)
