import one_time_protection

email_id = ""   # Your email ID
email_pass = ""   # Your generated app password


otp = one_time_protection.OTP(email_id,email_pass)

reciver_add = input("Enter your email: ")

otp.send_otp(reciver_add)

