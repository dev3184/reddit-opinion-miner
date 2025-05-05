import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download("stopwords")
nltk.download("punkt_tab")
nltk.download("wordnet")

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Function to clean Reddit text
def clean_text(text):
    if isinstance(text, str):  # Check if text is valid
        text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
        text = re.sub(r"@\w+|\#\w+", "", text)  # Remove mentions and hashtags
        text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters and numbers
        text = text.lower().strip()  # Convert to lowercase and remove spaces
        tokens = word_tokenize(text)  # Tokenization
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]  # Lemmatization
        return " ".join(tokens)
    return ""

# Load Reddit dataset
df = pd.read_csv("Path to your raw dataset")  # Change to your actual file name

# Print columns to verify correct names
print("Columns in dataset:", df.columns)

# Apply cleaning function using correct column name
if "Text" in df.columns:
    df["Cleaned_Text"] = df["Text"].apply(clean_text)
else:
    print("Error: Column 'Text' not found in dataset. Check column names.")

# Save cleaned data
df.to_csv("path to save the preprocessed dataset", index=False)

print("Reddit dataset cleaned successfully!")
