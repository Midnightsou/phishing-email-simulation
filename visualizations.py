import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.metrics import confusion_matrix
import os
import numpy as np

# Create outputs directory
os.makedirs('outputs', exist_ok=True)

print("Loading models and data...")
with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('models/nb_model.pkl', 'rb') as f:
    nb_model = pickle.load(f)

with open('models/test_data.pkl', 'rb') as f:
    X_test, y_test, y_pred = pickle.load(f)

# Load full dataset for word clouds
df = pd.read_csv('dataset.csv')
df['text'] = df['subject'] + ' ' + df['body']

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

print("\n1. Creating confusion matrix...")
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=['legitimate', 'phishing'])
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Legitimate', 'Phishing'],
            yticklabels=['Legitimate', 'Phishing'])
plt.title('Confusion Matrix - Phishing Email Detection', fontsize=16, fontweight='bold')
plt.ylabel('Actual Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('outputs/confusion_matrix.png', dpi=300)
print("✓ Saved: outputs/confusion_matrix.png")
plt.close()

print("2. Creating word clouds...")
# Word Cloud for Phishing Emails
phishing_text = ' '.join(df[df['label'] == 'phishing']['text'])
wordcloud_phishing = WordCloud(width=800, height=400, 
                               background_color='white',
                               colormap='Reds',
                               max_words=100).generate(phishing_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud_phishing, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Phishing Emails', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('outputs/wordcloud_phishing.png', dpi=300)
print("✓ Saved: outputs/wordcloud_phishing.png")
plt.close()

# Word Cloud for Legitimate Emails
legit_text = ' '.join(df[df['label'] == 'legitimate']['text'])
wordcloud_legit = WordCloud(width=800, height=400,
                            background_color='white',
                            colormap='Greens',
                            max_words=100).generate(legit_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud_legit, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Legitimate Emails', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('outputs/wordcloud_legitimate.png', dpi=300)
print("✓ Saved: outputs/wordcloud_legitimate.png")
plt.close()

print("3. Creating feature importance chart...")
# Feature Importance
feature_names = vectorizer.get_feature_names_out()
phishing_idx = list(nb_model.classes_).index('phishing')
feature_log_prob = nb_model.feature_log_prob_[phishing_idx]

# Get top 15 features
top_indices = feature_log_prob.argsort()[-15:][::-1]
top_features = [feature_names[i] for i in top_indices]
top_scores = [feature_log_prob[i] for i in top_indices]

plt.figure(figsize=(10, 8))
colors = plt.cm.Reds(np.linspace(0.4, 0.8, len(top_features)))
plt.barh(range(len(top_features)), top_scores, color=colors)
plt.yticks(range(len(top_features)), top_features)
plt.xlabel('Log Probability', fontsize=12)
plt.title('Top 15 Features Indicating Phishing Emails', fontsize=16, fontweight='bold')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('outputs/feature_importance.png', dpi=300)
print("✓ Saved: outputs/feature_importance.png")
plt.close()

print("4. Creating performance metrics chart...")
# Performance Metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='phishing')
recall = recall_score(y_test, y_pred, pos_label='phishing')
f1 = f1_score(y_test, y_pred, pos_label='phishing')

metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
values = [accuracy, precision, recall, f1]

plt.figure(figsize=(10, 6))
colors = ['#2ecc71', '#3498db', '#e74c3c', '#f39c12']
bars = plt.bar(metrics, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
plt.ylim(0, 1.0)
plt.ylabel('Score', fontsize=12)
plt.title('Model Performance Metrics', fontsize=16, fontweight='bold')
plt.axhline(y=0.8, color='gray', linestyle='--', alpha=0.5, label='80% threshold')

# Add value labels on bars
for bar, value in zip(bars, values):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.2%}',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.legend()
plt.tight_layout()
plt.savefig('outputs/performance_metrics.png', dpi=300)
print("✓ Saved: outputs/performance_metrics.png")
plt.close()

print("5. Creating combined visualization...")
# Combined visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Phishing Email Detection - Complete Analysis', fontsize=18, fontweight='bold', y=0.995)

# 1. Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=['legitimate', 'phishing'])
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0, 0],
            xticklabels=['Legitimate', 'Phishing'],
            yticklabels=['Legitimate', 'Phishing'])
axes[0, 0].set_title('Confusion Matrix', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('Actual Label', fontsize=11)
axes[0, 0].set_xlabel('Predicted Label', fontsize=11)

# 2. Performance Metrics
bars = axes[0, 1].bar(metrics, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
axes[0, 1].set_ylim(0, 1.0)
axes[0, 1].set_ylabel('Score', fontsize=11)
axes[0, 1].set_title('Performance Metrics', fontsize=14, fontweight='bold')
axes[0, 1].axhline(y=0.8, color='gray', linestyle='--', alpha=0.5)
for bar, value in zip(bars, values):
    height = bar.get_height()
    axes[0, 1].text(bar.get_x() + bar.get_width()/2., height,
                   f'{value:.1%}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 3. Top Phishing Features
top_10_features = top_features[:10]
top_10_scores = top_scores[:10]
colors_feat = plt.cm.Reds(np.linspace(0.4, 0.8, len(top_10_features)))
axes[1, 0].barh(range(len(top_10_features)), top_10_scores, color=colors_feat)
axes[1, 0].set_yticks(range(len(top_10_features)))
axes[1, 0].set_yticklabels(top_10_features, fontsize=9)
axes[1, 0].set_xlabel('Log Probability', fontsize=11)
axes[1, 0].set_title('Top 10 Phishing Indicators', fontsize=14, fontweight='bold')
axes[1, 0].invert_yaxis()

# 4. Dataset Distribution
labels_count = df['label'].value_counts()
colors_pie = ['#e74c3c', '#2ecc71']
axes[1, 1].pie(labels_count, labels=['Phishing', 'Legitimate'], autopct='%1.0f%%',
              colors=colors_pie, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
axes[1, 1].set_title('Dataset Distribution', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('outputs/complete_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: outputs/complete_analysis.png")
plt.close()

print("\n" + "="*50)
print("All visualizations created successfully!")
print("="*50)
print("\nGenerated files:")
print("  • outputs/confusion_matrix.png")
print("  • outputs/wordcloud_phishing.png")
print("  • outputs/wordcloud_legitimate.png")
print("  • outputs/feature_importance.png")
print("  • outputs/performance_metrics.png")
print("  • outputs/complete_analysis.png")