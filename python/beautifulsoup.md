# Beautifulsoup cheatsheet by Ehsan Shirzadi

### Prepare your soup:
```python
from bs4 import BeautifulSoup
with open("index.html") as fp:
    soup = BeautifulSoup(fp)
soup = BeautifulSoup("<html>a web page</html>",'html.parser')
```
### Find class using beautiful soup
```python
mydivs = soup.findAll("div", {"class": "stylelistrow"})
```
### Loop through items in HTML using beautiful soup
```python
for item in soup.select(".odd,.even"):
    print(item)
```

Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
