"""
A program that scans your email for messages containing bittorent links.
The email must be sent from a trusted sender (i.e. you), and contain a
password somewhere in the email that is set by you. 

The link can be sent to another program to open up, for example.
"""

import imapclient
import pyzmail
import re

# set email domain server -- varies but currently only supports gmail
domain = 'imap.gmail.com'

# define email and password for later use (command args)
email = ''
password = ''
secretCode = ''


"""
Strips the contents of msg for a magnet link. Msg should be an object returned 
by pyzmail.
"""


def stripBodyForLink(msg):
    magnet = re.split(r'\s', msg)
    for item in magnet:
        if '<magnet' in item.strip():
            magnetLink = item.strip('<>')
    if magnetLink != None:
        print('Magnet link found! ' + magnetLink)
        return magnetLink
    return 'Could not parse'


"""
Search INBOX folder in email for messages containing a secret code and
a provided email. imapObj should be returned from imapclient lib.
"""


def searchInbox(imapObj):
    imapObj.select_folder('INBOX', readonly=False)
    # search for emails from myself containing a special password
    mID = imapObj.search([u'FROM', email, u'TEXT', secretCode])
    # grab the raw message for decoding.
    rawMessage = imapObj.fetch(mID, ['BODY[]'])
    return rawMessage


"""
Uses pyzmail to decode an ugly message returned from imapLib. Returns the body
of the message.
"""


def decodeMessage(raw):
    msg = pyzmail.PyzMessage.factory(raw[list(raw.keys())[0]][b'BODY[]'])
    # return the body of the message.
    return msg.text_part.get_payload().decode(msg.text_part.charset)


"""
Log into email server with email and password. If domain is gmail,
an app password must be used if 2FA is enabled on the account.
"""


def loginIMAP():
    try:
        # login to IMAP client to read emails
        imapObj = imapclient.IMAPClient(domain, ssl=True)
        imapObj.login(email, password)
        return imapObj
    except Exception as e:
        print(e)
        exit(-1)


"""
User input to grab email, password, and secret code used to check for correct emails.
Note: application specific password is required for gmail if 2FA is used.
"""


def getInfo():
    global email, password, secretCode
    email = input("Please enter your email: example@domain.com\n")
    password = input("Please enter your password for your email\n")
    secretCode = input(
        "Please enter a secret code to scan for in your emails.\n")


getInfo()
imap = loginIMAP()
rawMsg = searchInbox(imap)
formattedMsg = decodeMessage(rawMsg)
link = stripBodyForLink(formattedMsg)
