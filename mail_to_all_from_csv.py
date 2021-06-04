import smtplib, ssl, csv

# Actual Message format
message = """\
From: {sender}
To: {email}
Subject: Your Grades

Hi, {name} Your grade is {grade}.
"""

# Sender Email ID & Password
sender = input('Enter Sender gmail : ')
password = input('Enter your password : ')

context = ssl.create_default_context()  # Getting  encryption context

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    print('Successfully Logged In..')

    # Importing data from csv file one by one......
    with open('contact.csv')as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, grade in reader:
            server.sendmail(
                sender,
                email,
                message.format(
                    sender=sender,
                    email=email,
                    name=name,
                    grade=grade,
                )
            )
print('Mail Successfully sent..')

