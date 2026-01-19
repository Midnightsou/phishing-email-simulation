import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import pickle

# Sample test emails
SAMPLE_EMAILS = [
    ("URGENT: Verify Your Account", "Your account will be suspended in 24 hours. Click here to verify."),
    ("Monthly Statement Ready", "Your statement is now available. Log into your account to view it."),
    ("You Won $10,000!", "Claim your prize by providing your bank details immediately."),
    ("Team Meeting Tomorrow", "Reminder: Weekly team meeting tomorrow at 10 AM in Conference Room B."),
    ("Password Expiring Soon", "Your password expires in 2 hours. Reset now or lose access forever.")
]

class PhishingDetectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Email Detector")
        self.root.geometry("800x700")
        self.root.resizable(False, False)
        
        # Load models
        self.load_models()
        
        # Create GUI
        self.create_widgets()
    
    def load_models(self):
        """Load the trained model and vectorizer"""
        try:
            with open('models/vectorizer.pkl', 'rb') as f:
                self.vectorizer = pickle.load(f)
            with open('models/nb_model.pkl', 'rb') as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "Model files not found. Please run train_model.py first.")
            self.root.destroy()
    
    def create_widgets(self):
        """Create GUI widgets"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', pady=15)
        title_frame.pack(fill='x')
        
        title = tk.Label(title_frame, text="🛡️ Phishing Email Detector", 
                        font=('Arial', 20, 'bold'), fg='white', bg='#2c3e50')
        title.pack()
        
        subtitle = tk.Label(title_frame, text="Analyze emails for phishing attempts", 
                           font=('Arial', 10), fg='#ecf0f1', bg='#2c3e50')
        subtitle.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Sample emails dropdown
        sample_frame = tk.Frame(main_frame)
        sample_frame.pack(fill='x', pady=(0, 15))
        
        tk.Label(sample_frame, text="Quick Test:", font=('Arial', 10, 'bold')).pack(side='left', padx=(0, 10))
        
        self.sample_var = tk.StringVar()
        sample_dropdown = ttk.Combobox(sample_frame, textvariable=self.sample_var, 
                                       values=[f"{i+1}. {s[0][:40]}..." for i, s in enumerate(SAMPLE_EMAILS)],
                                       state='readonly', width=50)
        sample_dropdown.pack(side='left', padx=(0, 10))
        
        load_btn = tk.Button(sample_frame, text="Load Sample", command=self.load_sample,
                            bg='#3498db', fg='white', font=('Arial', 9), cursor='hand2')
        load_btn.pack(side='left')
        
        # Subject input
        tk.Label(main_frame, text="Email Subject:", font=('Arial', 11, 'bold')).pack(anchor='w', pady=(10, 5))
        self.subject_entry = tk.Entry(main_frame, font=('Arial', 10), width=80)
        self.subject_entry.pack(fill='x', pady=(0, 15))
        
        # Body input
        tk.Label(main_frame, text="Email Body:", font=('Arial', 11, 'bold')).pack(anchor='w', pady=(0, 5))
        self.body_text = scrolledtext.ScrolledText(main_frame, font=('Arial', 10), 
                                                   height=8, wrap=tk.WORD)
        self.body_text.pack(fill='both', expand=True, pady=(0, 15))
        
        # Analyze button
        analyze_btn = tk.Button(main_frame, text="🔍 Analyze Email", command=self.analyze_email,
                               bg='#27ae60', fg='white', font=('Arial', 12, 'bold'),
                               cursor='hand2', pady=10)
        analyze_btn.pack(fill='x', pady=(0, 15))
        
        # Result frame
        self.result_frame = tk.Frame(main_frame, relief='solid', borderwidth=2, padx=15, pady=15)
        self.result_frame.pack(fill='x')
        
        self.result_label = tk.Label(self.result_frame, text="Results will appear here",
                                     font=('Arial', 10), fg='gray')
        self.result_label.pack()
        
        # Clear button
        clear_btn = tk.Button(main_frame, text="Clear All", command=self.clear_fields,
                             bg='#95a5a6', fg='white', font=('Arial', 9), cursor='hand2')
        clear_btn.pack(pady=(10, 0))
    
    def load_sample(self):
        """Load a sample email"""
        selection = self.sample_var.get()
        if selection:
            idx = int(selection.split('.')[0]) - 1
            subject, body = SAMPLE_EMAILS[idx]
            self.subject_entry.delete(0, tk.END)
            self.subject_entry.insert(0, subject)
            self.body_text.delete('1.0', tk.END)
            self.body_text.insert('1.0', body)
    
    def analyze_email(self):
        """Analyze the email"""
        subject = self.subject_entry.get().strip()
        body = self.body_text.get('1.0', tk.END).strip()
        
        if not subject or not body:
            messagebox.showwarning("Input Required", "Please enter both subject and body.")
            return
        
        # Predict
        text = subject + ' ' + body
        text_tfidf = self.vectorizer.transform([text])
        prediction = self.model.predict(text_tfidf)[0]
        probabilities = self.model.predict_proba(text_tfidf)[0]
        
        # Get confidence
        classes = self.model.classes_
        phishing_idx = list(classes).index('phishing')
        legit_idx = list(classes).index('legitimate')
        confidence = probabilities[phishing_idx] if prediction == 'phishing' else probabilities[legit_idx]
        
        # Get top features
        feature_names = self.vectorizer.get_feature_names_out()
        text_features = self.vectorizer.transform([text]).toarray()[0]
        top_indices = text_features.argsort()[-5:][::-1]
        top_features = [feature_names[i] for i in top_indices if text_features[i] > 0]
        
        # Display result
        self.display_result(prediction, confidence, top_features)
    
    def display_result(self, prediction, confidence, features):
        """Display the analysis result"""
        # Clear previous result
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        if prediction == 'phishing':
            self.result_frame.config(bg='#e74c3c')
            icon = "⚠️"
            result_text = "PHISHING EMAIL DETECTED"
            warning = "This email appears to be a phishing attempt. Do not click any links or provide personal information."
            color = 'white'
        else:
            self.result_frame.config(bg='#27ae60')
            icon = "✓"
            result_text = "LEGITIMATE EMAIL"
            warning = "This email appears to be safe."
            color = 'white'
        
        # Result header
        header = tk.Label(self.result_frame, text=f"{icon} {result_text}",
                         font=('Arial', 16, 'bold'), fg=color, bg=self.result_frame.cget('bg'))
        header.pack(pady=(0, 10))
        
        # Confidence
        confidence_label = tk.Label(self.result_frame, text=f"Confidence: {confidence:.1%}",
                                   font=('Arial', 11), fg=color, bg=self.result_frame.cget('bg'))
        confidence_label.pack(pady=(0, 10))
        
        # Warning
        warning_label = tk.Label(self.result_frame, text=warning, font=('Arial', 10),
                                fg=color, bg=self.result_frame.cget('bg'), wraplength=700)
        warning_label.pack(pady=(0, 10))
        
        # Key indicators
        if features:
            indicators_label = tk.Label(self.result_frame, text="Key indicators:",
                                       font=('Arial', 10, 'bold'), fg=color, 
                                       bg=self.result_frame.cget('bg'))
            indicators_label.pack(anchor='w', pady=(5, 5))
            
            for feature in features[:5]:
                feature_label = tk.Label(self.result_frame, text=f"  • {feature}",
                                        font=('Arial', 9), fg=color, 
                                        bg=self.result_frame.cget('bg'))
                feature_label.pack(anchor='w')
    
    def clear_fields(self):
        """Clear all input fields"""
        self.subject_entry.delete(0, tk.END)
        self.body_text.delete('1.0', tk.END)
        self.sample_var.set('')
        
        # Reset result frame
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        self.result_frame.config(bg='white')
        self.result_label = tk.Label(self.result_frame, text="Results will appear here",
                                     font=('Arial', 10), fg='gray')
        self.result_label.pack()

def main():
    root = tk.Tk()
    app = PhishingDetectorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()