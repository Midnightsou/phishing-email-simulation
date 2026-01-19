import pandas as pd
import csv

# Phishing emails (50 samples)
phishing_emails = [
    # Banking alerts (10)
    ("URGENT: Verify Your Account", "Your account has been compromised. Click here immediately to verify your identity or your account will be suspended within 24 hours.", "phishing"),
    ("Security Alert: Unusual Activity Detected", "We detected suspicious login attempts from unknown locations. Confirm your identity now to prevent account closure.", "phishing"),
    ("Your Bank Account is Locked", "Action required! Your account has been locked due to security reasons. Update your information here to restore access.", "phishing"),
    ("Confirm Your Banking Details", "Dear customer, we need you to confirm your banking details immediately. Failure to do so will result in account termination.", "phishing"),
    ("Unauthorized Transaction Alert", "We noticed an unauthorized transaction of $2,450. Click here to cancel this payment and secure your account now.", "phishing"),
    ("Account Verification Required", "Your account verification has expired. Please click the link below and re-enter your credentials to continue using our services.", "phishing"),
    ("Final Warning: Account Suspended", "This is your final notice. Your account will be permanently suspended if you don't verify your identity within 12 hours.", "phishing"),
    ("Fraud Alert - Action Needed", "Suspicious activity detected on your account. Verify your identity immediately by providing your full banking credentials.", "phishing"),
    ("Update Your Security Information", "For your security, please update your password and security questions by clicking here. Failure to comply will lock your account.", "phishing"),
    ("Critical: Confirm Your Identity", "We couldn't verify your identity. Click here and enter your account number, password, and SSN to avoid account closure.", "phishing"),
    
    # Prize notifications (10)
    ("Congratulations! You've Won $1,000,000", "You have been selected as our grand prize winner! Claim your prize now by providing your bank details for direct deposit.", "phishing"),
    ("You're Our Lucky Winner!", "Click here to claim your prize of $50,000. You must act within 24 hours or the prize goes to another participant.", "phishing"),
    ("Amazon Gift Card Winner", "Congratulations! You've won a $500 Amazon gift card. Click here and enter your payment information to cover shipping costs.", "phishing"),
    ("Lottery Winner Notification", "You won the international lottery! To claim your $2.5 million prize, please send us your banking information immediately.", "phishing"),
    ("Free iPhone 15 - Claim Now", "You've been chosen to receive a FREE iPhone 15 Pro Max! Just pay $9.99 shipping and confirm your credit card details.", "phishing"),
    ("Walmart Gift Card Giveaway Winner", "You won our $1000 Walmart gift card! Click to claim within 48 hours. Enter your personal details to verify eligibility.", "phishing"),
    ("WINNER: $5000 Cash Prize", "Congratulations! Your email was randomly selected. Claim your $5000 now by clicking here and providing verification details.", "phishing"),
    ("You've Won a Luxury Vacation", "Claim your all-expenses-paid trip to Hawaii! Just cover the registration fee by entering your credit card information here.", "phishing"),
    ("PayPal Prize Alert", "You've won $750 PayPal cash! To receive it, verify your PayPal account by logging in through this secure link immediately.", "phishing"),
    ("Exclusive Reward Waiting", "You've been specially selected for a $2000 reward. Claim now by confirming your identity and bank account details.", "phishing"),
    
    # Password/security urgency (10)
    ("Password Expiration Notice", "Your password will expire in 2 hours. Click here immediately to reset it or you'll lose access to your account permanently.", "phishing"),
    ("Security Update Required", "We've upgraded our security system. Reset your password now using this link or your account will be deleted tomorrow.", "phishing"),
    ("Change Your Password Immediately", "Your password has been compromised in a data breach. Click here and change it now to protect your account from hackers.", "phishing"),
    ("Username Update Required", "Due to new security policies, you must update your username within 24 hours. Click here and log in to make changes.", "phishing"),
    ("Your Account Will Be Deleted", "We will delete your account in 12 hours due to inactivity. Confirm your password here to keep your account active.", "phishing"),
    ("Suspicious Login Attempt", "Someone tried to access your account from Russia. Change your password immediately by clicking this link and logging in.", "phishing"),
    ("Password Reset Request", "We received a password reset request. If this wasn't you, click here immediately and verify your current credentials.", "phishing"),
    ("Security Breach Alert", "Your account was involved in a security breach. Reset your password and security questions now to prevent unauthorized access.", "phishing"),
    ("Mandatory Password Change", "As part of our security audit, you must change your password today. Use this link and enter your current password first.", "phishing"),
    ("Account Security Compromised", "Your security has been compromised. Verify your identity by entering your password, social security number, and date of birth.", "phishing"),
    
    # Delivery notifications (10)
    ("Package Delivery Failed", "We attempted to deliver your package but failed. Click here and confirm your address to reschedule delivery today.", "phishing"),
    ("UPS: Confirm Your Address", "Your package is waiting. Update your delivery address and pay the $3.99 redelivery fee to receive your shipment.", "phishing"),
    ("FedEx Delivery Pending", "Your package requires customs clearance. Pay the $15 fee here and provide your credit card details for immediate release.", "phishing"),
    ("DHL: Action Required", "Your parcel is on hold. Confirm your delivery details and pay the storage fee of $8.50 to avoid return to sender.", "phishing"),
    ("Amazon: Package Could Not Be Delivered", "We couldn't deliver your order. Click here to reschedule and verify your payment method for the delivery charge.", "phishing"),
    ("USPS Delivery Notice", "You have a package waiting at the post office. Confirm your identity here and pay the holding fee to collect it.", "phishing"),
    ("Your Shipment is Delayed", "Track your delayed package by clicking here and entering your credit card information to upgrade to express shipping.", "phishing"),
    ("Package Held at Customs", "Your international package is held at customs. Pay the clearance fee of $45 by entering your payment details here.", "phishing"),
    ("Delivery Attempt Failed - Redeliver", "We missed you! Reschedule your delivery by clicking here and confirming your address and payment information.", "phishing"),
    ("Final Notice: Package Return", "Your package will be returned in 24 hours. Prevent this by clicking here and updating your delivery preferences now.", "phishing"),
    
    # Tax/government scams (10)
    ("IRS: Tax Refund Approved", "You're eligible for a $2,847 tax refund. Click here to claim it by providing your bank account details for direct deposit.", "phishing"),
    ("Government Grant Approval", "You've been approved for a $15,000 government grant. Claim it now by verifying your social security number and bank info.", "phishing"),
    ("Stimulus Check Notification", "Your stimulus payment of $1,400 is ready. Enter your banking information here to receive your money immediately.", "phishing"),
    ("Tax Return Processing Error", "There was an error processing your tax return. Click here and re-enter your SSN and financial information to fix it.", "phishing"),
    ("IRS Account Suspended", "Your IRS account has been suspended due to suspicious activity. Verify your identity immediately to avoid legal action.", "phishing"),
    ("Unclaimed Tax Refund", "You have an unclaimed refund of $3,200. Click here within 48 hours and provide your bank details to receive payment.", "phishing"),
    ("Social Security Administration Alert", "Your social security benefits will be suspended. Call this number or click here to verify your SSN immediately.", "phishing"),
    ("Medicare Eligibility Update", "Update your Medicare information now. Click here and enter your social security number and date of birth to continue coverage.", "phishing"),
    ("Treasury Department Notice", "You owe back taxes. Pay immediately by clicking here or face legal prosecution and asset seizure within 72 hours.", "phishing"),
    ("Government Benefits Expiring", "Your benefits will expire unless you update your information. Click here and provide your SSN and bank account now.", "phishing"),
]

# Legitimate emails (50 samples)
legitimate_emails = [
    # Real bank notifications (10)
    ("Your Monthly Statement is Ready", "Your account statement for December is now available. Log into your account to view your transactions and balance.", "legitimate"),
    ("Low Balance Notification", "Your checking account balance has fallen below $100. Consider transferring funds to avoid any overdraft fees.", "legitimate"),
    ("Direct Deposit Confirmation", "A direct deposit of $2,500 has been added to your account ending in 4521. View details in your account dashboard.", "legitimate"),
    ("Credit Card Payment Due Reminder", "Your credit card payment of $145.50 is due on January 25th. Set up auto-pay to never miss a payment.", "legitimate"),
    ("New Account Feature Available", "We've added mobile check deposit to your account. Update your app to start depositing checks from your phone.", "legitimate"),
    ("Annual Account Review", "It's time for your annual account review. Schedule an appointment with your financial advisor through your online portal.", "legitimate"),
    ("Interest Rate Update", "The interest rate on your savings account has been adjusted to 2.5% APY effective February 1st.", "legitimate"),
    ("Paperless Statement Enrollment", "Go paperless and help the environment. Enroll in paperless statements through your account settings today.", "legitimate"),
    ("Fraud Protection Alert", "We blocked a suspicious transaction at an online merchant. If this was you, you can approve it through your mobile app.", "legitimate"),
    ("Account Anniversary", "Thank you for 5 years of banking with us! Check your account for a special loyalty bonus we've added.", "legitimate"),
    
    # Promotional emails (10)
    ("Weekly Newsletter - Tech Updates", "This week's top stories: New smartphone releases, AI developments, and the latest in cloud computing technology.", "legitimate"),
    ("30% Off Sale This Weekend", "Enjoy 30% off all items this Saturday and Sunday. Shop online or visit our stores. No code needed at checkout.", "legitimate"),
    ("New Product Launch", "Introducing our new winter collection. Browse the latest styles and find your perfect outfit for the season.", "legitimate"),
    ("Exclusive Member Discount", "As a valued member, enjoy an exclusive 20% discount on your next purchase. Offer valid until the end of the month.", "legitimate"),
    ("Recipe Ideas for the Week", "Try these delicious recipes this week: Monday - Pasta Primavera, Tuesday - Chicken Stir Fry, Wednesday - Vegetarian Tacos.", "legitimate"),
    ("Fitness Tips Newsletter", "5 tips to stay motivated this winter: Set realistic goals, find a workout buddy, track your progress, and more.", "legitimate"),
    ("Book Recommendations", "Based on your recent purchases, you might enjoy these new releases in mystery and thriller genres.", "legitimate"),
    ("Upcoming Webinar Invitation", "Join our free webinar on digital marketing strategies next Thursday at 2 PM EST. Register now to save your spot.", "legitimate"),
    ("Customer Appreciation Day", "You're invited to our customer appreciation event on February 15th. Enjoy refreshments and special in-store discounts.", "legitimate"),
    ("Seasonal Product Guide", "Spring is coming! Check out our guide to the best products for spring cleaning, gardening, and outdoor activities.", "legitimate"),
    
    # Work/professional emails (10)
    ("Team Meeting Tomorrow at 10 AM", "Reminder: Our weekly team meeting is scheduled for tomorrow at 10 AM in Conference Room B. Please review the agenda.", "legitimate"),
    ("Project Update Required", "Please submit your project status update by end of day Friday. Use the template provided in the shared drive.", "legitimate"),
    ("Quarterly Review Schedule", "Your quarterly performance review is scheduled for next week. Please complete your self-assessment form beforehand.", "legitimate"),
    ("Office Closure Notice", "The office will be closed on Monday, February 19th for Presidents' Day. Regular hours resume on Tuesday.", "legitimate"),
    ("New Employee Welcome", "Please join us in welcoming Sarah Johnson to the marketing team. Her first day is next Monday.", "legitimate"),
    ("IT System Maintenance", "Scheduled maintenance on our email servers will occur this Saturday from 2 AM to 6 AM. Services may be briefly interrupted.", "legitimate"),
    ("Deadline Extension Approved", "Your request for a deadline extension has been approved. The new due date is March 15th instead of March 1st.", "legitimate"),
    ("Training Session Registration", "Register for next month's professional development training on effective communication. Limited spots available.", "legitimate"),
    ("Company Policy Update", "Our remote work policy has been updated. Please review the changes in the employee handbook on the intranet.", "legitimate"),
    ("Team Lunch Next Friday", "Join us for a team lunch next Friday at 12:30 PM at Mario's Italian Restaurant. RSVP by Wednesday.", "legitimate"),
    
    # Service notifications (10)
    ("Your Subscription Renewal", "Your annual subscription will renew on February 1st for $99.99. Manage your subscription in account settings.", "legitimate"),
    ("Order Confirmation #12345", "Thank you for your order! Your items will ship within 2-3 business days. Track your package using the link below.", "legitimate"),
    ("Receipt for Your Purchase", "Here's your receipt for your purchase of $45.67 at Store Name on January 15th. Keep this for your records.", "legitimate"),
    ("Appointment Reminder", "This is a reminder of your appointment on Thursday, January 25th at 2:00 PM with Dr. Smith.", "legitimate"),
    ("Software Update Available", "A new version of our software is available. Update now to get the latest features and security improvements.", "legitimate"),
    ("Membership Renewal Notice", "Your gym membership expires in 30 days. Renew online to continue enjoying all our facilities and classes.", "legitimate"),
    ("Streaming Service Update", "We've added new content to your watchlist. Check out the latest movies and TV shows available now.", "legitimate"),
    ("Cloud Storage Upgrade", "You're using 80% of your cloud storage space. Upgrade to our premium plan for 1TB of storage at $9.99/month.", "legitimate"),
    ("Warranty Registration", "Register your recent purchase to extend your warranty by an additional 6 months at no cost.", "legitimate"),
    ("Auto-Pay Setup Confirmation", "You've successfully set up auto-pay for your monthly subscription. You'll be charged $19.99 on the 1st of each month.", "legitimate"),
    
    # Social media/app notifications (10)
    ("You Have 3 New Messages", "You have unread messages from your friends. Open the app to read and respond to them.", "legitimate"),
    ("Weekly Activity Summary", "You walked 42,000 steps this week! That's 15% more than last week. Keep up the great work!", "legitimate"),
    ("Photo Memories from Last Year", "Remember this day last year? Check out these photos from your trip to the beach.", "legitimate"),
    ("New Comment on Your Post", "Emily and 5 others commented on your recent post. See what they said.", "legitimate"),
    ("Friend Request from John Doe", "John Doe sent you a friend request. View their profile and decide whether to accept.", "legitimate"),
    ("App Update Available", "Version 3.2 of the app is available with bug fixes and performance improvements. Update now for the best experience.", "legitimate"),
    ("Your Weekly Podcast Digest", "New episodes from your favorite podcasts are available. Listen now to stay up to date.", "legitimate"),
    ("Security Settings Changed", "You recently changed your security settings. If this wasn't you, review your account security.", "legitimate"),
    ("New Follower Notification", "Sarah_designs started following you. Check out their profile.", "legitimate"),
    ("Content Recommendation", "Based on your interests, you might like these articles about technology and innovation.", "legitimate"),
]

# Combine all emails
all_emails = phishing_emails + legitimate_emails

# Create DataFrame
df = pd.DataFrame(all_emails, columns=['subject', 'body', 'label'])

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv('dataset.csv', index=False, quoting=csv.QUOTE_ALL)

print("Dataset created successfully!")
print(f"Total emails: {len(df)}")
print(f"Phishing emails: {len(df[df['label'] == 'phishing'])}")
print(f"Legitimate emails: {len(df[df['label'] == 'legitimate'])}")
print("\nFirst 5 rows:")
print(df.head())