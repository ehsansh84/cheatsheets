# HA Proxy cheatsheet by Ehsan Shirzadi

### Install HA proxy:
```
apt install -y haproxy
```


### Edit `/etc/haproxy/haproxy.cfg` and add:
```
global
  stats socket /var/run/haproxy.stat level admin mode 600

frontend kubernetes-frontend
    bind 172.16.16.100:6443
    mode tcp
    option tcplog
    default_backend kubernetes-backend

backend kubernetes-backend
    mode tcp
    option tcp-check
    balance roundrobin
    server kmaster1 172.16.16.101:6443 check fall 3 rise 2
    server kmaster2 172.16.16.102:6443 check fall 3 rise 2
```


### Restart the service:
```
systemctl restart haproxy
```


Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
