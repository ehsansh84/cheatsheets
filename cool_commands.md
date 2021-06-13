# Cool terminal commands cheatsheet by Ehsan Shirzadi

### Terminal commands:

Want to know your public IP?
### wget -qO - icanhazip.com

Remove all files but one?
### rm -v !("filename")

Remove all files but two?
### rm -v !("filename1"|"filename2") 

Remove all files but two types?
### rm -v !(*.zip|*.odt)

Rename terminal window
echo $'\033]30;NewName\007'

List all files but *conf
### ls -I "*conf"

list all files containing my_text
###grep -iRl "my_text" *

get certificate:
```
certbot certonly -d domain —expand -d www.domain.com
```

See listening ports:
```
ss -tulpn
```

Echo with a typewriter effect:
```
apt install pv
echo "You can simulate on-screen typing just like in the movies" | pv -qL 10
```

Grep lines before and after:
```
grep -A 5 keyword filename #after
grep -B 5 keyword filename #before
grep -C 5 keyword filename #center
```
Tunnel network traffic:
```
sudo sshuttle --dns -vvr root@x.x.x.x 0/0
```

### Problem with apt update?
```
printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
```
Change system DNS:
```
vim /etc/systemd/resolved.conf 
systemctl restart systemd-resolved.service 
```
###### Email: Ehsan.Shirzadi@Gmail.com
###### Web: www.ehsanshirzadi.com

