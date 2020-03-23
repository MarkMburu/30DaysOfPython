import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Enviromental variables look at sendgrid
username = 'mackryanlamar1@gmail.com'
password = '#Mack1789'

def send_mail(text = 'Email Body',subject='Hello World',from_email='Mark Mburu <mackryanlamr1@gmail.com>',to_emails=None,html=None):
    assert isinstance(to_emails,list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ",".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)    
    if html != None:
        html_part = MIMEText(html,'html')
        msg.attach(html_part)   

    msg_str = msg.as_string()
    #login to my smpt server
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()