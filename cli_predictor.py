import pickle
import numpy as np

# Sample test emails for quick demo
SAMPLE_EMAILS = [
    {
        "subject": "URGENT: Verify Your Account Now",
        "body": "Your account will be suspended in 24 hours. Click here immediately to verify your identity."
    },
    {
        "subject": "Your Monthly Statement is Ready",
        "body": "Your account statement for this month is now available. Log into your account to view transactions."
    },
    {
        "subject": "Congratulations! You've Won $10,000",
        "body": "You've been selected as our prize winner! Click here and provide your bank details to claim your prize."
    },
    {
        "subject": "Team Meeting Tomorrow",
        "body": "Reminder: Our weekly team meeting is scheduled for tomorrow at 10 AM. Please review the agenda."
    },
    {
        "subject": "Password Expiration Warning",
        "body": "Your password will expire in 2 hours. Reset it now or lose access to your account permanently."
    }
]

def load_models():
    """Load the trained model and vectorizer"""
    try:
        with open('models/vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        with open('models/nb_model.pkl', 'rb') as f:
            model = pickle.load(f)
        return vectorizer, model
    except FileNotFoundError:
        print("Error: Model files not found. Please run train_model.py first.")
        exit(1)

def predict_email(subject, body, vectorizer, model):
    """Predict if an email is phishing or legitimate"""
    text = subject + ' ' + body
    text_tfidf = vectorizer.transform([text])
    
    # Get prediction and probability
    prediction = model.predict(text_tfidf)[0]
    probabilities = model.predict_proba(text_tfidf)[0]
    
    # Get class indices
    classes = model.classes_
    phishing_idx = list(classes).index('phishing')
    legit_idx = list(classes).index('legitimate')
    
    confidence = probabilities[phishing_idx] if prediction == 'phishing' else probabilities[legit_idx]
    
    # Get top contributing features
    feature_names = vectorizer.get_feature_names_out()
    text_features = vectorizer.transform([text]).toarray()[0]
    
    # Get top 5 features with highest TF-IDF scores
    top_indices = text_features.argsort()[-5:][::-1]
    top_features = [(feature_names[i], text_features[i]) for i in top_indices if text_features[i] > 0]
    
    return prediction, confidence, top_features

def display_prediction(subject, body, prediction, confidence, features):
    """Display prediction results in a formatted way"""
    print("\n" + "="*60)
    print("EMAIL ANALYSIS")
    print("="*60)
    print(f"\nSubject: {subject}")
    print(f"Body: {body[:100]}..." if len(body) > 100 else f"Body: {body}")
    print("\n" + "-"*60)
    
    if prediction == 'phishing':
        print("⚠️  RESULT: PHISHING EMAIL DETECTED")
        print(f"Confidence: {confidence:.1%}")
        print("\n🚨 WARNING: This email appears to be a phishing attempt!")
    else:
        print("✓ RESULT: LEGITIMATE EMAIL")
        print(f"Confidence: {confidence:.1%}")
        print("\n✅ This email appears to be safe.")
    
    if features:
        print("\nKey indicators:")
        for i, (feature, score) in enumerate(features[:5], 1):
            print(f"  {i}. '{feature}' (weight: {score:.3f})")
    
    print("="*60)

def main():
    print("\n" + "="*60)
    print("PHISHING EMAIL DETECTOR - CLI")
    print("="*60)
    
    print("\nLoading trained model...")
    vectorizer, model = load_models()
    print("✓ Model loaded successfully!\n")
    
    while True:
        print("\nOptions:")
        print("  1. Test a sample email")
        print("  2. Enter your own email")
        print("  3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\nSample Emails:")
            for i, email in enumerate(SAMPLE_EMAILS, 1):
                print(f"  {i}. {email['subject'][:50]}...")
            
            sample_choice = input("\nSelect a sample (1-5): ").strip()
            try:
                idx = int(sample_choice) - 1
                if 0 <= idx < len(SAMPLE_EMAILS):
                    email = SAMPLE_EMAILS[idx]
                    prediction, confidence, features = predict_email(
                        email['subject'], email['body'], vectorizer, model
                    )
                    display_prediction(email['subject'], email['body'], 
                                     prediction, confidence, features)
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == '2':
            print("\nEnter email details:")
            subject = input("Subject: ").strip()
            body = input("Body: ").strip()
            
            if subject and body:
                prediction, confidence, features = predict_email(
                    subject, body, vectorizer, model
                )
                display_prediction(subject, body, prediction, confidence, features)
            else:
                print("Error: Both subject and body are required.")
        
        elif choice == '3':
            print("\nThank you for using the Phishing Email Detector!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()