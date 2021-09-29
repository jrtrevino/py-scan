# About
This program will scan a user's emails for messages containing magnet URIs. These magnet URIS can be compiled into a list for further use.
## Dependencies

First, install pip if you haven't. More info here:
https://pypi.org/project/pip/

Second, ensure your version of Python is 3.6+. 

Next install pyzmail36 (for Python 3.6+)
``` 
$ pip install pyzmail36.
```

Lastly, ensure imapclient is installed.
```
$ pip install imapclient
```

## More info
The program requires three pieces of information from the user:
  1. email <string>
  2. password <string>
  3. secret <string>
  
This program scans emails for messages containing <secret> from the provided email.
This is to prevent random magnet downloads from arbitrary people.
