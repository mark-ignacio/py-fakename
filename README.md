py-fakename
===========
[![Build Status](https://travis-ci.org/mark-ignacio/py-fakename.svg?branch=master)](https://travis-ci.org/mark-ignacio/py-fakename)

py-fakename is a simple little package that gets identities generated from [https://fakena.me](https://fakena.me). 

Requirements
------------

* Python 2.7, 3.3+
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
