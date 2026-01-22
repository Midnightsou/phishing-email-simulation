🛡️ Phishing Email Detection System

A machine learning–based system that simulates phishing email detection using Naive Bayes classification and TF-IDF feature extraction.


🎯 Overview

This project demonstrates how machine learning can be used to detect phishing emails by analyzing email subject lines and message content. It provides a simple but effective simulation of how automated phishing detection systems work in real-world cybersecurity applications.

Objectives

Create a labeled dataset of phishing and legitimate emails

Train a machine learning classifier for phishing detection

Extract textual features using TF-IDF

Evaluate model performance using accuracy metrics

Simulate phishing detection through user input

✨ Features
Core Features

Machine Learning–Based Detection using Naive Bayes

TF-IDF Feature Extraction for text analysis

Binary Classification (Phishing vs Legitimate)

Command-Line Prediction Tool

Simple GUI Prediction Interface

Accuracy Evaluation and Reporting

Dataset

Small labeled dataset of email samples

Two classes:

Phishing emails

Legitimate emails

Email text and subject lines used as features

📁 Project Structure

phishing-detector/
│
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── QUICKSTART.md                 # Quick setup guide
│
├── generate_dataset.py           # Creates email dataset
├── dataset.csv                   # Generated email samples
│
├── train_model_enhanced.py       # Enhanced multi-model training
├── visualizations_enhanced.py    # Comprehensive visualizations
│
├── cli_predictor.py              # Command-line interface
├── gui_predictor.py              # Graphical user interface
│
├── models/                       # Saved models (auto-created)
│   ├── vectorizer.pkl
│   ├── naive_bayes_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   ├── best_model.pkl
│   └── test_data.pkl
│
├── outputs/                      # Visualizations (auto-created)
│   ├── model_comparison.png
│   ├── confusion_matrices_all.png
│   ├── wordclouds_comparison.png
│   ├── feature_importance_top20.png
│   ├── cross_validation_comparison.png
│   └── comprehensive_dashboard.png
│
└── reports/                      # Evaluation reports (auto-created)
    └── evaluation_report.txt

🚀 Installation
Prerequisites

Python 3.8 or higher

pip package manager

Step 1: Clone the Repository
git clone https://github.com/Midnightsou/phishing-email-simulation.git
cd phishing-email-simulation

Step 2: Install Dependencies
pip install -r requirements.txt


Main Dependencies

-pandas

-scikit-learn

-numpy

-matplotlib

💻 Usage
Complete Workflow
1. Generate the Dataset
python generate_dataset.py


Creates dataset.csv containing labeled email samples.

2. Train the Model
python train_model.py


This will:

Load the dataset

Convert text data to TF-IDF vectors

Train a Naive Bayes classifier

Evaluate accuracy

Save the trained model and vectorizer

3. Test the System

Command-Line Interface

python cli_predictor.py


Enter custom email text

Receive phishing or legitimate prediction

Graphical Interface

python gui_predictor.py


Simple GUI for non-technical users

Displays prediction result clearly

🔬 Models & Methodology
Feature Extraction

TF-IDF (Term Frequency–Inverse Document Frequency)

Converts email text into numerical feature vectors

Reduces importance of common words

Highlights distinctive phishing-related terms

Machine Learning Model
Naive Bayes (MultinomialNB)

Suitable for text classification problems

Fast and lightweight

Performs well with TF-IDF features

Used as the primary classifier in this project

Evaluation Metric

Accuracy: Measures overall correctness of predictions

📊 Results

The trained model successfully classifies phishing and legitimate emails.

Accuracy demonstrates that even simple machine learning techniques can effectively detect phishing patterns.

Performance depends on dataset size and diversity.

Sample Output

Model Accuracy: 95%
Prediction: Phishing Email

📈 Visualization

Basic evaluation results are displayed during training

Optional charts can be generated using matplotlib

Output files are saved in the outputs/ directory

🔮 Future Improvements

Expand dataset size for better generalization

Add URL and domain analysis

Detect HTML-based phishing content

Train and compare multiple models

Integrate deep learning models (LSTM, BERT)

Deploy as a web API or browser extension

Integrate with real email systems

🤝 Contributing

Contributions are welcome. You may:

Improve dataset quality

Add new phishing patterns

Enhance model evaluation

Improve UI/UX

Optimize performance

📄 License

This project is intended for educational and research purposes.

👤 Author

Developed as a cybersecurity and machine learning simulation project.

Last Updated: January 2025
Version: 1.0
