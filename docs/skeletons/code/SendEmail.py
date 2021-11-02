def sendEmail(receiver, itemName, url):
    """
    Sends the notification email to the user.
    Takes in the user's email, product name, and product url as input.
    In order to send the email, please prepare an email account and
    fill in the gmail_user for email address and gmail_password for password.

    :param receiver: The email address of the receiver(User)
    :param itemName: The name of the the product
    :param url: URL of the product
    :return: 1 if the email sent successfully, 0 if not
    """
