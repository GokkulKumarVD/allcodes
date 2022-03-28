import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
print("hey")
fromaddr = "cc.automation@swiggy.in"
toaddr = ['vd.gokkulkumar@swiggy.in', 'sourav.verma@swiggy.in']
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)
msg['Subject'] = "Marvex code requires attention "
body = "Tickets are going beyong 30,000. Please exceed my limit"
msg.attach(MIMEText(body, 'plain'))
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "xcdbqpvdmzvckhwh")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()