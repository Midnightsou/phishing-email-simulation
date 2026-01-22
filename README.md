Phishing Email Detection Simulation Using Machine Learning
📖 Overview
This project simulates a machine learning workflow for cybersecurity, specifically focusing on the detection of phishing emails. By analyzing email content and subject lines, the system classifies messages into two categories: Phishing and Legitimate.

Designed for educational and research purposes, this project demonstrates the end-to-end process of dataset creation, feature extraction (TF-IDF), model training (Naive Bayes), and evaluation. It includes both a Command Line Interface (CLI) and a Graphical User Interface (GUI) for real-time predictions.

🎯 Objectives
Dataset Creation: Generate a labeled dataset of phishing and legitimate emails.

Model Training: Train a machine learning model using Natural Language Processing (NLP) techniques.

Simulation: Mimic real-world phishing detection scenarios.

Evaluation: Assess performance using Accuracy, Precision, Recall, and F1-Score.

Interactivity: Provide tools (CLI & GUI) for user interaction and testing.

🛠 Technologies Used
The project is built using Python and the following libraries:

Core: Python, NumPy, Pandas

Machine Learning & NLP: scikit-learn

Visualization: Matplotlib, Seaborn

GUI: Tkinter (standard Python GUI)

📂 Project Structure
Plaintext

phishing-email-simulation/
│
├── dataset.csv              # Generated email dataset
├── generate_dataset.py      # Script to generate synthetic data
├── train_model.py           # Script to train and save the ML model
├── cli_predictor.py         # Command-line tool for prediction
├── gui_predictor.py         # Graphical interface for prediction
├── visualizations.py        # Script to generate performance charts
├── requirements.txt         # Python dependencies
├── models/                  # Directory for saved .pkl models
└── outputs/                 # Directory for results and graphs
🚀 Installation
1. Clone the Repository
Bash

git clone https://github.com/Midnightsou/phishing-email-simulation.git
cd phishing-email-simulation
2. Install Dependencies
Ensure you have Python installed, then install the required packages:

Bash

pip install -r requirements.txt
💻 Usage
Follow these steps to run the simulation from start to finish.

Step 1: Generate Dataset
Create the synthetic dataset of emails.

Bash

python generate_dataset.py
Step 2: Train the Model
Train the Naive Bayes classifier on the generated dataset.

Bash

python train_model.py
Step 3: Run Predictions
You can test the model using either the command line or the GUI.

Option A: CLI Mode

Bash

python cli_predictor.py
Option B: GUI Mode

Bash

python gui_predictor.py
Step 4: Visualize Results
Generate confusion matrices and performance graphs.

Bash

python visualizations.py
🧠 Machine Learning Approach
Feature Extraction
Text Preprocessing: Tokenization and stop-word removal.

Vectorization: Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text data into numerical vectors.

Algorithm
Naive Bayes Classifier: Selected for its efficiency and effectiveness in text classification tasks.

Evaluation Metrics
The model is evaluated based on:

Accuracy

Precision

Recall

F1-Score

📊 Results
The system successfully distinguishes between phishing and legitimate emails with high accuracy. While results depend on the dataset size and variety, the visualizations generated in the outputs/ folder provide a detailed breakdown of model performance.

🔮 Roadmap & Limitations
Limitations
Dataset: Currently relies on a small, synthetic dataset.

Features: Limited to text-based features (body/subject) without analyzing headers.

Integration: Not connected to live email servers (IMAP/SMTP).

Future Improvements
[ ] Integrate a larger, real-world dataset (e.g., Enron or PhishTank).

[ ] Implement advanced NLP models (BERT, LSTM).

[ ] Add URL and domain reputation analysis.

[ ] Analyze email headers for spoofing.

[ ] Develop a web-based API (FastAPI/Flask).

📄 License
This project is intended for educational purposes only.
