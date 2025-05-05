from transformers import pipeline
import pandas as pd
from tqdm import tqdm

# Load your Reddit data (assuming CSV with a 'text' column)
df = pd.read_csv("Your Location to find cleaned reddit dataset")
df = df.dropna(subset=['Cleaned_Text'])

# Reduce to manageable length (truncate too-long comments to prevent errors)
MAX_CHARS = 1000
df['Cleaned_Text'] = df['Cleaned_Text'].apply(lambda x: x[:MAX_CHARS] if len(x) > MAX_CHARS else x)

# Convert to list
texts = df['Cleaned_Text'].tolist()

# Load sentiment classifier with PyTorch backend
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", framework="pt")

# To handle large datasets safely: batch inference
results = []
batch_size = 32

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i+batch_size]
    try:
        out = classifier(batch, truncation=True)  # Add truncation here
        results.extend(out)
    except Exception as e:
        print(f"Error at batch {i}: {e}")
        # Skip this batch if it crashes
        results.extend([{"label": "ERROR", "score": 0.0}] * len(batch))

# Add results to DataFrame
df = df.iloc[:len(results)].copy()  # trim df if needed
df['sentiment'] = [r['label'] for r in results]
df['confidence'] = [r['score'] for r in results]
print("Saving now...")
# Save the labeled dataset
df.to_csv("Your Location to save labeled dataset", index=False)

print("Sentiment analysis completed and saved.")
