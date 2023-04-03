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
```python
import requests
import socks
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 5000)
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url=url)
print(response.json())
```
Test proxy is working using this code getting public IP:
```python
import requests
url = "https://httpbin.org/ip"
response = requests.get(url=url)
public_ip = response.json()['origin']
print("Your public IP address is:", public_ip)
response = requests.get(url=url, proxies={'http': 'socks5://127.0.0.1:5000', 'https': 'socks5://127.0.0.1:5000'})
public_ip = response.json()['origin']
print("Your public IP address is:", public_ip)
```
The output should be like this:
```
Your public IP address is: YOUR_PUBLIC_IP
Your public IP address is: YOUR_PROXY_IP
```
