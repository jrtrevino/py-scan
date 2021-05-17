# About
This program will scan a user's emails for messages containing magnet URIs. Eventually, the link will be passed
to another program that will open up qbittorent and add the magnet link to the download queue.

## dependencies
First, install pip if you haven't. More info here:
https://pypi.org/project/pip/

Second, ensure your version of python is 3.6+. Next install pyzmail36
### pip install pyzmail36.

The 36 represents python version 3.6.

Lastly, ensure imapclient is installed.
### pip install imapclient

## More info
The program requires three pieces of information from the user:
  1. email <string>
  2. password <string>
  3. secret <string>
  
This program scans emails for messages containing <string> secret from the provided email.
This is to prevent random magnet downloads from arbitrary people.

Yes, this program does require you to email yourself, but that is another story.
