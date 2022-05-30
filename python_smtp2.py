import smtplib
from email.message import EmailMessage

my_email = EmailMessage()
my_email['from'] = 'Dayton Braison'
my_email['to'] = 'ymarquez1995@gmail.com'
my_email['subject'] = ':)'

my_email.set_content("Hello")

with smtplib.SMTP("smtp.gmail.com") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pythonemailtesting666@gmail.com', 'db231989')
    smtp.send_message(my_email)
    print('Success!!')