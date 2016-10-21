import smtplib as s
import getpass
import sys
import traceback

def main():
    print("Enter in your email and password\n\r")
    global username
    global password
    username = input("Gmail username: ")
    password = getpass.getpass(prompt = "Gmail password: ")

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
        msg = input("What is the header?:\n ")
        msg += '\n ' + input("What are we sending them?:\n ")
        spam(amount, email, msg)
        print ("Your email(s) has been sent to"), email
        more  = input("Would you like to send anymore emails?:\n ")
        loop = (more.lower().strip() == "y" or "yes"  or "fuckyeah")


def sms():
    carrier_address = "a"

    print ("""What carrier?
            1.AT&T
            2.SPRINT
            3.T-MOBILE
            4.VERIZON
            """)
    carrier = int(input())
    if carrier == 1:
        carrier_address = "@txt.att.net"

    if carrier == 2:
        carrier_address = "@messaging.sprintpcs.com"

    if carrier == 3:
        carrier_address = "@tmomail.net"

    if carrier == 4:
        carrier_address = "@vtext.com"

    amountsms = int(input("How many do you want to send?"))
    phone = input("Phone number: ") + str(carrier_address)
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
    server.quit()
main()
