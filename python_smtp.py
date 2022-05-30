import smtplib

# sender email & passworddb23
my_email = "pythonemailtesting666@gmail.com"
my_password = input('Enter your password: ')


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="daytonbraison@gmail.com", 
    msg="Subject:Hello World!!\n\nI am available for work!")
