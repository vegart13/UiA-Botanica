#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import smtplib

#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#Email SETUP
smtp_username = "uia.botanica1@gmail.com" # This is the username used to login to your SMTP provider
smtp_password = "crumb2019" # This is the password used to login to your SMTP provider
smtp_host = "smtp.gmail.com" # This is the host of the SMTP provider
smtp_port = 587 # This is the port that your SMTP provider uses

smtp_sender = "uia.botanica1@gmail.com" # This is the FROM email address
smtp_receivers = ['xuw@live.no'] # This is the TO email address

message_dead = """From: Sender Name <uia.botanica1@gmail.com>
To: Receiver Name <xuw@live.no>
Subject: Moisture Sensor Notification
Warning, no moisture detected! Plant death imminent!!! :'(
"""

# This is the message that will be sent when moisture IS detected again

message_alive = """From: Sender Name <uia.botanica1@gmail.com>
To: Receiver Name <xuw@live.no>
Subject: Moisture Sensor Notification
Panic over! Plant has water again :)
"""
def sendEmail(smtp_message):
	try:
		smtpObj = smtplib.SMTP(smtp_host, smtp_port)
		smtpObj.login(smtp_username, smtp_password) # If you don't need to login to your smtp provider, simply remove this line
		smtpObj.sendmail(smtp_sender, smtp_receivers, smtp_message)
		print ("Successfully sent email")
	except smtplib.SMTPException:
		print ("Error: unable to send email")

def callback(channel):
        if GPIO.input(channel):
                print ("Water Detected!" + GPIO.IN)
                sendEmail:message_dead
        else:
                print ("Water Detected!")
                sendEmail:message_alive

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
