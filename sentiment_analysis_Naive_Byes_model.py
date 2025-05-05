from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# 1. Load dataset
df = pd.read_csv("Path to your labeled reddit dataset")

# Optional: Drop rows with missing comments or labels
df = df.dropna(subset=["Cleaned_Text", "sentiment"])

# 2. Encode labels to numbers
label_encoder = LabelEncoder()
df['encoded_sentiment'] = label_encoder.fit_transform(df['sentiment'])

# 3. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['Cleaned_Text'], df['encoded_sentiment'], test_size=0.2, random_state=42)

# 4. Vectorize text using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Train Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train_vec, y_train)

# 6. Predict on test set
y_pred = nb_model.predict(X_test_vec)

# 7. Evaluate
# Assuming y_test and y_pred are already defined
# Here Evalution is stored in Evalution Folder
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=nb_model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Naive Bayes")
plt.show()
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))
