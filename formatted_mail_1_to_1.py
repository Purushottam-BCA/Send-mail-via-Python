import smtplib, ssl
from email.mime.text import MIMEText   # MIMEText class contain body info. of email
from email.mime.multipart import MIMEMultipart  # This class contains attachments, Headers etc.
from email import encoders  # Encoding of attachment
from email.mime.base import MIMEBase # It will contain attachment

# STEP-1 : Connecting to mail server

smtp_server = 'smtp.gmail.com'  # Smtp server of gmail
port = 465  # Port No. for SSL (Secure socket layer)

# Sender Email ID & Password
sender = input('Enter Sender gmail : ')
password = input('Enter your password : ')

# Reciever Email Id
reciever = input('Enter reciever email : ')

# because 2 different msg will be sent, 1. html supported else 2. plain text.
message = MIMEMultipart('alternative')

# ----------- Email headers ----------
message['Subject'] = 'Just Sending Msg ONE to ONE'
message['From'] = sender
message['To'] = reciever

# -------- Plain text (If HTML not supported) ---------
txt = """\
Hi, Its me.

My name is Purushottam Kumar. """

# -------- Formatted Text (If HTML Supported) -----------
html = """\
<html>
 <body>
  <b> <p> Hi, <br>
      How are You ? <br> </b>
        Check Out my its source code at <a href="https://github.com/Purushottam-BCA"> Github </a>
   </p> 
</body>
</html>
"""

part1 = MIMEText(txt, 'plain')
part2 = MIMEText(html, 'html')

# File (attachment) to be sent
file_name = 'coder.jpg'

# Opening file & Reading binary data of attachment
with open(file_name, 'rb') as attachment:
    part_a = MIMEBase('application', 'octet-stream') # Created a new MIMEBase
    part_a.set_payload(attachment.read())

encoders.encode_base64(part_a)   # Encoded to base64

# Some header info. about attachment
part_a.add_header(
    'Content-Disposition',
    f'attachment; filename = {file_name}',
)

message.attach(part1)
message.attach(part2)   # If it fails then it will go to part1
message.attach(part_a)  # If it fails then it will go to part2

context = ssl.create_default_context()  # Getting  encryption context

# Method-1 : Secured and encrypted connection from start (Port-465)
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('Successfully Logged In..')
    # Sending mail here.
    server.sendmail(sender, reciever, message.as_string())

'''
# Method-2 : Start with Unencrypted Connection later convert to encrypted form (Port-587)

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() # Extended version of hello to server
    server.starttls(context=context)
    server.login(sender, password)
    print('Successfully Logged In..')
    server.sendmail(sender, reciever, message.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()
'''



