# NordVpn 
An OpenVpn from NordVpn:
https://support.nordvpn.com/Restricted-countries/1396307432/Connecting-from-countries-with-internet-restrictions-on-Linux.htm

If Whoops then:
```
sudo rm -rf ~/.config/nordvpn
```
reboot system
```
nordvpn whitelist add port 8282 22 8585
```
Login legacy (No need to open website):
```
nordvpn login --legacy
```
Change protocol:
```
nordvpn set protocol TCP
nordvpn set protocol UDP
```
Support recommendations:
nordvpn whitelist add subnet 192.168.0.0/16
