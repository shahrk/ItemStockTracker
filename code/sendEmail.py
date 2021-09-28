import smtplib


def sendEmail(receiver, itemName, url):
    gmail_user = 'ncsuemailtest@gmail.com'
    gmail_password = 'NCSU2021'

    subject = "The item " + itemName + " is restocked!!!!!"
    body = "The item " + itemName + " at " + url + " has been restocked."
    email_text = """From: Your ItemStockTracker 
To: %s
Subject: %s
%s
    """ % (receiver, subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(gmail_user, receiver, email_text)
        smtp_server.close()
        print("You've Got Mail!")
    except Exception as ex:
        print("Whoops….", ex)
