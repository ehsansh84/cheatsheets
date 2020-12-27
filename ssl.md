
get certificate:
```
certbot certonly -d domain —expand -d www.domain.com
```


get certificate expiration date:
```
openssl x509 -enddate -noout -in fullchain.pem
```


