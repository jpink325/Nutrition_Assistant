
from email.message import EmailMessage
import ssl
import cred
import schedule
import time
import smtplib

def sendWeeklyMessage():
    email_sender = cred.userNime
    email_password = cred.passWird
    email_receiver = cred.userNime

    subject = 'A Brief Grocery Goal Check-in'
    words = """
    Good morning, hope you're enjoying yourself. This is a brief reminder to achieve
    your goals by being consistent with your budget and nutrition choices. If you're
    experiencing any challenges, just know that we've got your back!!
    
    Click the link below for some inspiration: 
    
    https://giphy.com/gifs/minions-dancing-minionsboogie-dancingminions-0UUjywKBYQpM6xCTeg
     """


    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(words)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def sendMonthlySurvey():
    email_sender = cred.userNime
    email_password = cred.passWird
    email_receiver = cred.userNime
    subject = 'Reminder to Fill Out Your Survey with Us!!!'
    words = """
       Every month, we try our best to improve your experience for the best price and quality.
       To continue this, we'd love to hear from you. To access the suvvey, click the link below:
       
       https://docs.google.com/forms/d/e/1FAIpQLSeq-UfIoiKamKSDk93MPJfWLdr9JINMDnGstoEEc9gq9ycvAg/viewform?usp=pp_url
       """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(words)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

#schedule.every().monday.at('09:00').do(sendWeeklyMessage)
#schedule.every(28).days.do(sendMonthlySurvey)
schedule.every().monday.at('21:09:00').do(sendWeeklyMessage)

while True:
    schedule.run_pending()
    time.sleep(1)


