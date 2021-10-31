# Issuing SSL Certificates using certbot by Ehsan Shirzadi
get certificate:
```
certbot certonly -d domain —expand -d www.domain.com
```

get certificate expiration date:
```
openssl x509 -enddate -noout -in fullchain.pem
```

Renew all certificates:
```
certbot renew --webroot-path /usr/share/nginx/html/cdn
```

Use certbot to test to prevent reaching the limits only add `--dry-run` for this purpose

###Get certificate using DNS Challenge:
```
certbot certonly -d *.domain.com --manual --preferred-challenges dns
```
It shows a key and value like:
```
_acme-challenge.shirzadi.ir
RvQ08kL5HOx82iqJyehetJ2yp-Epq5gRzqm2kFha_cI
```

In mx toolbox using TXT lookup you can check that the value is set or not:
```
https://mxtoolbox.com
```

If you want to do it with a docker container:
```
sudo docker run -it --rm --name certbot -v "/volumes/certbot/letsencrypt:/etc/letsencrypt" -v "/volumes/certbot/var/lib/letsencrypt:/var/lib/letsencrypt" certbot/certbot certonly -d *.3dworld.ir --expand -d 3dworld.ir  --manual --preferred-challenges dns
```

Create a DNS record with type of Text. set the key and value.
Then proceed in cert bot. That's it!
