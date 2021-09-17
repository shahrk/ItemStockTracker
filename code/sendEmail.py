import smtplib

gmail_user = 'ncsuemailtest@gmail.com'
gmail_password = '********'

sender = gmail_user
receiver = ['*********@gmail.com']
subject = 'Have a good day'
body = 'today''s lucky number is 777'

email_text = """\
Subject: %s
%s
""" % (subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sender, receiver, email_text)
    smtp_server.close()
    print ("You've Got Mail!")
except Exception as ex:
    print ("Whoops….",ex)