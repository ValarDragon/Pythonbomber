import smtplib as s
import getpass
import sys
import traceback
import configparser
import logging
from logging.config import fileConfig

#http://stackoverflow.com/questions/19379120/how-to-read-a-config-file-using-python
def setupLogging():
    fileConfig('logging.conf')
    global logger
    logger = logging.getLogger("root.main")
    logger.debug("Program started")

def startup():
    global username
    global password

    global config
    config = configparser.ConfigParser()
    config.read('config.ini')

    if('username' in config['email']):
        username = config['email']['username']
        print("hello " + username)
    else:
        print("Enter in your gmail username\n\r")
        username = input("Gmail username: ")

    if('password' in config['email']):
        password = config['email']['password']
    else:
        print("Enter in your gmail password\n\r")
        password = getpass.getpass(prompt = "Gmail password: ")

    global isLogging
    if('1' in config['email']['logging']):
        isLogging = True
        setupLogging()
    else:
        isLogging = False
    main()

def main():
    print ("""What do you want to bomb?
        1. Email
        2. SMS

        """)

    option = int(input())
    if(option==1):
        email()
    elif(option==2):
        sms()

def email():
    loop = 1
    while (loop == 1):
        amount = int(input("How many emails do you want to send?:\n "))
        email = input("What's their email?:\n ")
        if(not ("@" in email)):
            contactbook = config._sections['contact_book']
            if(email.lower().strip() in contactbook):
                email = contactbook[email.lower().strip()]

        subject = input("What is the subject line of your message?:\n ")
        msg = input("What are we sending them?:\n ")

        if("," in email):
            email = email.split(',')
            for i in (email):
                spam(amount, i, formatMessage(subject,msg,i))
        else:
            spam(amount, email, formatMessage(subject,msg,email))
        print(("Your email(s) has been sent to %s") % str(email))

def formatMessage(subject,msg,email):
    headers = ["from: " + username,
                   "to: " + email,
                   "subject: " + subject,
                   "content_type: text/html"]
    headers = "\r\n".join(headers)
    headers += "\r\n\r\n" + msg
    return headers

def sms():
    phone = input("Phone number: ")
    if(re.search('[a-zA-Z]', phone)):
        contactbook = config._sections['contact_book']
        if(phone.lower().strip() in contactbook):
            phone = contactbook[phone.lower().strip()]
    else:
        carrier_address = ""

        print ("""What carrier?
                1.AT&T
                2.SPRINT
                3.T-MOBILE
                4.VERIZON
                """)
        carrier = int(input())
        if carrier == 1:
            carrier_address = "@txt.att.net"
        elif carrier == 2:
            carrier_address = "@messaging.sprintpcs.com"
        elif carrier == 3:
            carrier_address = "@tmomail.net"
        elif carrier == 4:
            carrier_address = "@vtext.com"
        phone += str(carrier_address)

    amountsms = int(input("How many texts do you want to send?"))
    message = input("Message: ")

    spam(amountsms,phone,message)
    print("Sending messages...")

def spam(num, email, msg):
    server = s.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)

    for i in range(num):
        try:
            print(email)
            server.sendmail(username, email, msg)
        except:
            print(str(traceback.format_exc()))
    if(isLogging):
        logger.debug(str(num) + ' email(s) sent to ' + email + ' with content ' + msg)
    server.quit()

startup()
