import smtplib
from email import encoders
# To encode file attachment 
from email.mime.text import MIMEText
# Handle plain text 
from email.mime.base import MIMEBase
# Handle attachment
from email.mime.multipart import MIMEMultipart
# Handle mails containing multiple content: text and attachment

server = smtplib.SMTP_SSL('smtp.zoho.eu', 465)
# Connect to the SMTP service provided by the mail provider
#Zoho Mail est un bon service de mail car il autorise les connections via SMTP sans payer, ave uniquement le mail et le mdp

server.ehlo()
# Send HELO to identify the client to the SMTP server

with open('password.txt', 'r') as f:
    password = f.read()

server.login('putyourmail@zohomail.eu', password)

msg = MIMEMultipart()
msg['From'] = 'putyourmail@zohomail.eu'
msg['To'] = 'receiver@zohomail.eu'
msg['Subject'] = 'Just a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')
 # Read Bit for a photo
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
# Convert binary data into a text format for the attachment (image) to be properly sent with SMTP
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
# Convert the entire mail into a string
server.sendmail('putyourmail@zohomail.eu', 'receiver@zohomail.eu', text)

server.quit()
