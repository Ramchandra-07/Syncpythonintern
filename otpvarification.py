import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for _ in range(6):
    OTP += random.choice(digits)

otp = OTP + " is your OTP"
msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

emailid = input("Enter your email: ")
password = input("Enter your password: ")

s.login(emailid, password)
s.sendmail(emailid, emailid, msg)
s.quit()

entered_otp = input("Enter your OTP: ")
if entered_otp == OTP:
    print("Verified")
else:
    print("Please check your OTP again")



