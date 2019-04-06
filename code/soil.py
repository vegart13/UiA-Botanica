#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import smtplib
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#Email Setup
smtp_username = ""#the address the email is being sent from
smtp_password = ""#password to that email
smtp_host = "smtp.gmail.com" #smtp server for your email service (this case gmail)
smtp_port = 587 #port for the smtp server(This case gmail)

smtp_sender = "" # This is the FROM email address
smtp_receivers = "" # This is the TO email address
#change reciever email above and below on both variables
message_dead = "Needs Water"

# This is the message that will be sent when moisture IS detected again


def sendEmail(smtp_message):
    try:
        smtpObj = smtplib.SMTP(smtp_host, smtp_port)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(smtp_username, smtp_password) # If you don't need to login to your smtp provider, simply remove this line
        smtpObj.sendmail(smtp_sender, smtp_recievers, smtp_message)
        smtpObj.quit()
        print ("Successfully sent email")
    except smtplib.SMTPException:
        print ("Error: unable to send email")



def callback(channel):
        if GPIO.input(channel):
                str(GPIO.input(channel))
                print ("Water Detected!")
                
                
        else:
                print ("Water Not Detected!")
                
                sendEmail(message_dead)
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(3600)
