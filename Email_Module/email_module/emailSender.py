import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(serverLink,password,subject,msg,sender,receivers):
    '''
    :param serverLink: e.g. smtp.gmail.com:587
    :param password: The password of the sender
    :param subject: The subject of the email
    :param msg: The body of the email
    :param sender: The sender email address
    :param receivers: List of receivers email address
    :return: None
    '''
    try:

        body = email.message.Message()
        body['Subject'] = subject
        body.add_header('Content-Type', 'text/html')
        body.set_payload(f'{msg}')
        server = smtplib.SMTP(serverLink)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receivers,  body.as_string())
        server.quit()
        print(f"Msj sent to: {receivers} ")

    except NameError:
        print(f"Something went wrong :( {NameError}")

def send_email_attached(serverLink,password,subject,msg,sender,receivers,attachedfile,attachedfileName='file.pdf'):
    '''
    :param serverLink: e.g. smtp.gmail.com:587
    :param password: The password of the sender
    :param subject: The subject of the email
    :param msg: The body of the email
    :param sender: The sender email address
    :param receivers: List of receivers email address
    :param attachedfile: Attached file
    :param attachedfileName: Name Attached file with extension: default *.pdf
    :return: None
    '''
    try:
        # instance of MIMEMultipart
        msgMultipart = MIMEMultipart()

        # storing the subject
        msgMultipart['Subject'] = subject

        # string to store the body of the mail
        body = msg

        # attach the body with the msg instance
        msgMultipart.attach(MIMEText(body, 'html')) #it accepts html

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachedfile).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % attachedfileName)

        # attach the instance 'p' to instance 'msg'
        msgMultipart.attach(p)

        server = smtplib.SMTP(serverLink)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receivers,  msgMultipart.as_string())
        server.quit()
        print(f"Msj sent to: {receivers} ")

    except NameError:
        print(f"Something went wrong :( {NameError}")


#from this tutorial
#https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/

