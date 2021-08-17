# wget cheatsheet by Ehsan Shirzadi

### How to set proxy inline:
```
 wget https://speed.hetzner.de/1GB.bin -e use_proxy=yes -e https_proxy=SERVER_IP:3128
```
### For all users of the system via the `/etc/wgetrc` or for the user only with the `~/.wgetrc` file:
```
use_proxy=yes
http_proxy=SERVER_IP:8080
https_proxy=SERVER_IP:8080
```

Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
