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

Grep lines before and after:
```
grep -A 5 keyword gilename #after
grep -B 5 keyword gilename #before
grep -C 5 keyword gilename #center
```

### Problem with apt update?
```
printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
```

###### Email: Ehsan.Shirzadi@Gmail.com
###### Web: www.ehsanshirzadi.com

