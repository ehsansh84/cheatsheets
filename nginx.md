# Docker cheatsheet by Ehsan Shirzadi

### Some usefull commands:
Reload configurations: `nginx -s reload`
Test configurations: `nginx -t`

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

### Config to use reverse proxy:
```
server {
    listen       80;
    listen  [::]:80;
    server_name  domain.com;
    location / {
        proxy_pass          http://localhost:8080;
        proxy_http_version  1.1;
        proxy_set_header    Upgrade     $http_upgrade;
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

### Config to load HTML:
```
server {
    listen       80;
    listen  [::]:80;
    server_name  domain.com;
    root /var/www/html;
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```
