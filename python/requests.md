Get a URL using proxy:
```python
import requests
url = 'https://jsonplaceholder.typicode.com/posts/1'
proxy = {
    'http': 'http://127.0.0.1:5000',
    'https': 'http://127.0.0.1:5000'
}
response = requests.get(url=url, proxies=proxy)
print(response.json())
```
Get a URL using `socks` proxy:
```
import requests
import socks
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 5000)
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url=url)
print(response.json())
```
