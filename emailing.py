import smtplib
import imghdr
from email.message import EmailMessage

GOOGLE_PW = "wsztyouktahtucli"
SENDER = "namanmaulikshah@gmail.com"
RECEIVER = "namanmaulikshah@gmail.com"


def send_email(image_path, sender=SENDER, receiver=RECEIVER, password=GOOGLE_PW):
    print("Send email function started. ")
    email_message = EmailMessage()
    email_message["Subject"] = "Object appeared in the room!"
    email_message.set_content("Hey we just saw this new object in the room!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password=password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()
    print("Send email function ended")


if __name__ == "__main__":
    send_email(image_path="images/trial.png")
