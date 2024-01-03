# pip

## [ReadTimeoutError: HTTPSConnectionPool(host='pypi.python.org', port=443) with pip?](https://stackoverflow.com/questions/43298872/how-to-solve-readtimeouterror-httpsconnectionpoolhost-pypi-python-org-port)

Use <mark style="color:yellow;">`--default-timeout=100`</mark> parameter with the install:

```python
sudo pip install --default-timeout=100 future
```
