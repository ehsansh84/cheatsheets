# How to recover Ubuntu's lost password?

### Boot up using a live ubuntu, then check `/etc/shadow`
Since this file belongs to the live Ubuntu, you can not see your ubuntu users here.  
Then mount you previous root for example `/dev/sda3`:
```
mount /dev/sda3 /mnt
```
Then change root to this directory:
```
chroot /mnt
```
Now your live ubuntu is using your old root directory. so you can use commands like `passwd` or `add user`  
Finally reboot and login you os using new credentials.

