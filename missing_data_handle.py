import pandas as pd

# Load the dataset
df = pd.read_csv("path to your raw dataset or preprocessed dataset")

# Remove rows where "Comments" is empty or NaN
df = df[df["Cleaned_Text"].notna()]  # Removes NaN values
df = df[df["Cleaned_Text"].str.strip() != ""]  # Removes empty strings

# Save the cleaned dataset
df.to_csv("Your cleaned dataset location to save", index=False)

print("Removed empty comments. Cleaned dataset saved as cleaned_sentiment_data_no_empty_comments.csv")
