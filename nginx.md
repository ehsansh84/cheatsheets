# Docker cheatsheet by Ehsan Shirzadi

### Some usefull commands:
```
```




### Config to force SSL:
```
server {
    listen       80;
    listen  [::]:80;
    server_name  domain.co www.domain.co;
    return 301 https://$host$request_uri;
}

server {
    listen       443;
    listen  [::]:443;
    server_name  domain.co www.domain.co;
    ssl_certificate     /etc/letsencrypt/live/domain.co/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.co/privkey.pem;
}

```
