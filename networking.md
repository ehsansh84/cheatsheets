# Networking cheatsheet by Ehsan Shirzadi

### Forward requests from public IP to local network:
```
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o public_interface -j MASQUERADE
iptables -A FORWARD -i public_interface -o local_interface -m state  --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i local_interface -o public_interface -j ACCEPT
```
### Forward ssh from port 3101 to port 22 of a local computer:
```
iptables -t nat -A POSTROUTING --out-interface public_interface -j MASQUERADE
iptables -A FORWARD --in-interface local_interface -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -i local_interface -m tcp --dport 25 -j DNAT --to-destination local_ip:22
```

Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
