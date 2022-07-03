import smtplib
from random import randint
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class OTP:

    def __init__(self,sender_email,sender_pass):
        self.__sender_email = sender_email
        self.__no_of_tries = 3
        self.__email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.__email_server.login(sender_email, sender_pass)

    def send_otp(self,reciever_email=None):
        otp = self.generate_otp()

        if reciever_email is None:
            reciever_email = input("Please verify your email address: ")


        msg = self.create_msg(otp,reciever_email)
        self.__email_server.send_message(msg)

        print("OTP sent successfully!!!")

        print("------------------------------------------------")
        print("To resend OTP, press 1")
        print("To change email address, press 2")
        print("------------------------------------------------")

        for _ in range(self.__no_of_tries):
            input_otp = input("Please enter OTP or Above options: ")        

            if input_otp == "1":
                print("\n\n")
                self.send_otp(reciever_email=reciever_email)
                return True

            if input_otp == "2":
                print("\n\n")
                self.send_otp()
                return True

            if input_otp == str(otp):
                print("Your email is verified!!!")
                self.__email_server.quit()
                return True

            print("Incorrect OTP!!!")

        print("You are unauthorized")
        self.__email_server.quit()
        return False


    def create_msg(self,otp,reciever_email):
        style1 = "text-align: center; font-size: 20px;"
        style2 = "font-weight: bold; font-size: 20px;"
        style3 = "font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;"
         
        msg_html = f"""
            <html>
            <head>
            <style>
            p {style1}
            span {style2}
            html {style3}
            </style>
            </head>
            <body>
                <p>The verification code is: <span>{otp}</span></p>
            </body>
            </html>
            """

        msg = MIMEMultipart('related')
        msg['Subject'] = "Verify your email"
        msg['From'] = self.__sender_email
        msg['To'] = reciever_email
        msg_html = MIMEText(msg_html, 'html')
        msg.attach(msg_html)

        return msg


    def generate_otp(self):
        OTP = randint(100000,999999)
        return OTP
