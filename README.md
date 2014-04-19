python-utrace
=============

Python wrapper for [utrace.de](http://en.utrace.de/api.php) XML API.

* __Author__: Ondrej Sika, <http://ondrejsika.com>, <ondrej@ondrejsika.com>
* __GitHub__: <https://github.com/ondrejsika/python-utrace>
* __PyPI__: <http://pypi.python.org/pypi/utrace>
* __LICENSE__: [MIT](LICENSE)


## Install


```
pip install utrace
```


## Usage

``` python
>>> import utrace
>>> utrace.utrace('8.8.8.8')
[{'countrycode': 'US',
  'host': None,
  'ip': '8.8.8.8',
  'isp': 'Level 3 Communications',
  'latitude': 38,
  'longitude': -97,
  'org': 'Google',
  'queries': 7,
  'region': None,
  'result': '\n'}]
>>> utrace.utrace('google.com')
[{'countrycode': 'US',
  'host': 'google.com',
  'ip': '173.194.70.102',
  'isp': 'Google',
  'latitude': 37.419200897217,
  'longitude': -122.05740356445,
  'org': 'Google',
  'queries': 8,
  'region': 'Mountain View',
  'result': '\n'}]
```

