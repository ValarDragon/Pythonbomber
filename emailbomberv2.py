
#ChangeLog: Added user and password input


#import sys
import smtplib as s
import getpass
def spam(num, email, msg, username, password):
    for i in range(num):
        server = s.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(email, email, msg)

loop = 1

print("Enter in your email and password\n\r")

username = input("Gmail username: ")
password = getpass.getpass(prompt = "Gmail password: ")

print ("""What do you want to bomb?
    1.Email
    2.SMS
        
    """)

option = input()

if option == 1:
    while (loop == 1):
        amount = int(input("How many emails do you want to send?: "))
        email = input("What's their email?: ")
        msg = input("What are we sending them?: ")
        spam(amount, email, msg, username, password)
        print ("Your email(s) has been sent to"), email
        more  = input("Would you like to send anymore emails?: ")
        loop = (more.lower().strip() == "y" or "yes"  or "fuckyeah")



if option == 2:
    carrier_address = 0

    print ("""What carrier?
            1.AT&T
            2.SPRINT
            3.T-MOBILE
            4.VERIZON
            """)
    carrier = input()

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

    while(loop == 1): 
        server.sendmail(username,phone,message)
    print("Sending messages...")


