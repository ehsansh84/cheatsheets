# Cool terminal commands cheatsheet by Ehsan Shirzadi

### Terminal commands:

Want to know your public IP?
### wget -qO - icanhazip.com

Remove all files but one?
### rm -v !("filename")

Base64 Encode
### echo string_to_encode | base64

Base64 Decode
### echo ZWhzYW5zaDg0Okp1Y2lhbEB4NjQ= | base64 --decode

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

Change timzone for ubuntu
```
sudo timedatectl set-timezone Asia/Tehran
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
Hard disk performance test:
```
fio --loops=5 --size=1024m --filename=/mnt/nfs/test12.txt --stonewall --ioengine=libaio --direct=1 \
  --name=Seqread --bs=1m --rw=read \
  --name=Seqwrite --bs=1m --rw=write \
  --name=512Kread --bs=512k --rw=randread \
  --name=512Kwrite --bs=512k --rw=randwrite \
  --name=4kQD32read --bs=4k --iodepth=32 --rw=randread \
  --name=4kQD32write --bs=4k --iodepth=32 --rw=randwrite
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
Change system DNS another way:
```
vim /etc/systemd/resolved.conf 
systemctl restart systemd-resolved
```

Fix missing VPN client
```
sudo apt install network-manager-pptp-gnome
```
Find all sockets on your system:
```
sudo find / -type s
```
ls and numerical permissions:
```
 ls -l | awk '{k=0;for(i=0;i<=8;i++)k+=((substr($1,i+2,1)~/[rwx]/) \
             *2^(8-i));if(k)printf("%0o ",k);print}'
```
Unset env variables:
```
unset GNUPLOT_DRIVER_DIR
```
###### Email: Ehsan.Shirzadi@Gmail.com
###### Web: www.ehsanshirzadi.com

