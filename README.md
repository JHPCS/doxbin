# Doxbin ping script setup

First things first, pip install requests beautifulsoup4 in cmd prompt for scraping doxbin.
URL = "https://doxbin.com/" Just the URL of doxbin of course. 
SEARCH_TERM = "target_user/post" This is where you input what to search for on doxbin, so if youre scared of your name being leaked input that here, aswell as whatever game people could get it from or something. 
EMAIL_ADDRESS = "yourgmailaddress@gmail.com" This your email address to send to another email address the results, it will send a email to notify of the post being found. 
EMAIL_PASSWORD = "yourpassword" Just the app password of that email.
RECIPIENT_EMAIL = "recipient@example.com" This is the email address that gets the notification
SMTP_SERVER = "smtp.gmail.com" smtp for gmail.
SMTP_PORT = 587 Just the port. 
CHECK_INTERVAL_SECONDS = 600 This is 10 mins converted to seconds so it checks every 10 minutes. 
A side note for the sending email, you have to set it up with 2fa and have an app password for gmail, so you put that there instead of actual google pass. 
Now time for the cookies to bypass doxbin thinking you are a bot. Go to doxbin, dev tools, application, storage, cookies. 
cookies = {
    'XSRF-TOKEN': '',
    '__ddg1_': '',
    '__ddg2_': '',
    '__ddg3': '',
    '__ddg5_': '',
    '__ddgid_': '',
    '__ddgmark_': '',
    'doxbin_session': ''
}
Then locate the cookies with these names, for each cookie fill in the value that shows in your browser. Now every 24 hours you might have to change the values.

# Doxbin script to get dox removed

COMING SOON 
