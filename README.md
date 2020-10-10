## myUtils

Structured collection of functions that could be useful for every project.

### Installation

To install execute `pip install -r requirements.txt` from the project root.
Or `pip install --src "" "-r requirements.txt` from the project root for the src-less projects.


### Usage

Add into `requirements.txt` file:
````requirements.txt
-e git://github.com/yuriy-logosha/myutils.git#egg=myutils
````

### Examples of usage
````
from myutils import *
...
myrequests.get(...)
...
````
or
````
from myfile import json_from_file, json_to_file
from myparser import MyHTMLParser
from myrequests import get as _get
````

With `myosascript` we can execute any osascript on macOs and control execution.

With `mykeyboard_mac` we can automate keyboard by sending commands to press any key or combination of keys. 
For example, we can change input language or enter word into input field.

With `myrequests` we can make a GET calls, or we can make a several calls sharing same sassion. 
Very usefull while needed to keep cookies or for authentication purposes.  