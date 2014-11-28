py-fakename
===========
py-fakename is a simple little package that gets identities generated from [https://fakena.me](https://fakena.me). 

There are no additional dependencies past an installation of Python. py-fakename has only been tested on Python 2.7 and
Python 3.4, so your compatibility mileage may vary.

Requirements
------------

* Tested on Python 2.7 or Python 3.4
* The [requests](https://github.com/kennethreitz/requests) library

Installation
------------

To install py-fakename, run:
    
```bash
$ pip install py-fakename
```

Usage
-----

Return value reordered for clarity:

```python
>>> from pprint import pprint
>>> import fakename
>>> pprint(fakename.gen_identity())
{'name': 'Lucy Macias',
 'dob': datetime.date(1945, 11, 15),
 'address': '5261 Edens Court',
 'city': 'Wilmot',
 'state': 'NH',
 'zip': '03287',
 'phone': '(603) 687-4938',
 'username': 'lucymaciasn7T',
 'password': '9e4UD5JC5spCDtd',
 'temp_email': 'lucymaciasYwA@crazespaces.pw',
 'permalink': 'https://fakena.me/j/18c[snip]7095.html'}
```