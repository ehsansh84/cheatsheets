# Proxmox terminal commands cheatsheet by Ehsan Shirzadi

Backup a container in /var/lib/vz/dump
`vzdump 102` or `vzdump 102 --compress gzip`
where 102 is the ID of container

Restore a container:
`pct restore 200 vzdump-lxc-112-2020_07_19-12_28_51.tar.gz  --storage local-lvm`

See the list of containers:
```
pct list
```
Stop container with ID 102:
```
pct stop 102
```

Start container with ID 102:
```
vzctl start 102
```
Set the host name:
```
vzctl set 250 --hostname test2.example.com --save
```

Remove previous IP:
```
vzctl set 250 --ipdel 192.168.0.102 --save
```

Add new IP:
```
vzctl set 250 --ipadd 192.168.0.250 --save   
```


###### Email: Ehsan.Shirzadi@Gmail.com
###### Web: www.ehsanshirzadi.com
