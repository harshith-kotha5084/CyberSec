import smtplib
from email.mime.text import MIMEText

# Email configuration
sender_email = "harshith.kotha123@gmail.com"
receiver_email = "harshith.kotha5084@gmail.com"
subject = "Test Email"
body = "This is a plain text email sent from Python. user ='harsh'. pass='harsh'"

# Create a plain text email message
message = MIMEText(body)
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# SMTP server configuration
smtp_server = "kotha"  # Change to your SMTP server address or "localhost" if running locally
smtp_port = 25  # Port 25 for unencrypted SMTP

# Create an SMTP connection and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    server.quit()
