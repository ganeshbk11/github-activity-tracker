import requests
import smtplib
from email.mime.text import MIMEText

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    events = response.json()
    
    report = f"Weekly GitHub Activity for {username}:\n\n"
    
    for event in events[:10]:
        event_type = event['type']
        repo_name = event['repo']['name']
        date = event['created_at'][:10]
        report += f"- [{date}] {event_type} on {repo_name}\n"
    
    return report

def send_email(report):
    sender = "mrindia123aa@gmail.com"
    receiver = "mrindia123aa@gmail.com"
    app_password = "exsg saew tres yonf"
    
    msg = MIMEText(report)
    msg['Subject'] = "Your Weekly GitHub Activity Report"
    msg['From'] = sender
    msg['To'] = receiver
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, app_password)
        server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully!")

report = get_github_activity("ganeshbk11")
print(report)
send_email(report)