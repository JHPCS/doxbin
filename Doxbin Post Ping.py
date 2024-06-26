import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

URL = "https://doxbin.com/"
SEARCH_TERM = "target_user/post"
EMAIL_ADDRESS = "yourgmailaddress@gmail.com"
EMAIL_PASSWORD = "yourpassword"
RECIPIENT_EMAIL = "recipient@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
CHECK_INTERVAL_SECONDS = 600

# Replace the following with your actual cookies
cookies = {
    'cookie_name1': 'cookie_value1',
    'cookie_name2': 'cookie_value2',
    # Add all relevant cookies here
}

def check_for_post():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    session = requests.Session()
    response = session.get(URL, headers=headers, cookies=cookies)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Uncomment the following line to print the entire HTML content for debugging
        # print(soup.prettify())
        
        if SEARCH_TERM in soup.get_text():
            return True
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
    
    return False

def send_email():
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = "Doxbin Post Found"
    body = f"The post containing the term '{SEARCH_TERM}' has been found on {URL}."
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

while True:
    if check_for_post():
        send_email()
    else:
        print(f"No post containing '{SEARCH_TERM}' found.")
    time.sleep(CHECK_INTERVAL) # type: ignore
