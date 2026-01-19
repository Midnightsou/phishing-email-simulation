import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

print("Loading dataset...")
df = pd.read_csv('dataset.csv')

# Combine subject and body for better classification
df['text'] = df['subject'] + ' ' + df['body']

print(f"Dataset loaded: {len(df)} emails")
print(f"Phishing: {len(df[df['label'] == 'phishing'])}")
print(f"Legitimate: {len(df[df['label'] == 'legitimate'])}")

# Prepare features and labels
X = df['text']
y = df['label']

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"\nTraining set: {len(X_train)} emails")
print(f"Test set: {len(X_test)} emails")

# Create TF-IDF vectorizer
print("\nCreating TF-IDF features...")
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english', ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print(f"Features created: {X_train_tfidf.shape[1]} features")

# Train Naive Bayes classifier
print("\nTraining Naive Bayes classifier...")
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)

# Make predictions
y_pred = nb_model.predict(X_test_tfidf)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='phishing')
recall = recall_score(y_test, y_pred, pos_label='phishing')
f1 = f1_score(y_test, y_pred, pos_label='phishing')

print("\n" + "="*50)
print("MODEL PERFORMANCE")
print("="*50)
print(f"Accuracy:  {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall:    {recall:.2%}")
print(f"F1-Score:  {f1:.2%}")

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred, labels=['legitimate', 'phishing'])
print(f"                Predicted")
print(f"                Legit  Phishing")
print(f"Actual Legit    {cm[0][0]:5d}  {cm[0][1]:5d}")
print(f"       Phishing {cm[1][0]:5d}  {cm[1][1]:5d}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Get feature importance (top words indicating phishing)
print("\n" + "="*50)
print("TOP 15 PHISHING INDICATORS")
print("="*50)

# Get feature names and their importance
feature_names = vectorizer.get_feature_names_out()
phishing_idx = list(nb_model.classes_).index('phishing')
feature_log_prob = nb_model.feature_log_prob_[phishing_idx]

# Get top features for phishing
top_phishing_indices = feature_log_prob.argsort()[-15:][::-1]
print("\nWords/phrases most indicative of PHISHING:")
for i, idx in enumerate(top_phishing_indices, 1):
    print(f"{i:2d}. {feature_names[idx]}")

# Get top features for legitimate
legitimate_idx = list(nb_model.classes_).index('legitimate')
feature_log_prob_legit = nb_model.feature_log_prob_[legitimate_idx]
top_legit_indices = feature_log_prob_legit.argsort()[-15:][::-1]
print("\nWords/phrases most indicative of LEGITIMATE:")
for i, idx in enumerate(top_legit_indices, 1):
    print(f"{i:2d}. {feature_names[idx]}")

# Save the model and vectorizer
print("\n" + "="*50)
print("SAVING MODEL")
print("="*50)

with open('models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
print("✓ Vectorizer saved to models/vectorizer.pkl")

with open('models/nb_model.pkl', 'wb') as f:
    pickle.dump(nb_model, f)
print("✓ Model saved to models/nb_model.pkl")

# Save test data for visualization
with open('models/test_data.pkl', 'wb') as f:
    pickle.dump((X_test, y_test, y_pred), f)
print("✓ Test data saved to models/test_data.pkl")

print("\nTraining complete! You can now run the predictor scripts.")