# How to run a V2Ray server?
## Method 1:
```
sudo apt update
sudo apt install -y docker.io
sudo apt install -y docker-compose
wget https://raw.githubusercontent.com/SonyaCore/vmess-deploy/main/deploy.sh
bash deploy.sh
```
Copy the output into your v2ray client, something like this:
```
vmess://eyJhZGQiOiIxNjcuMjM1LjE1Ny4yMDgiLCAiYWlkIjoiMCIsICJob3N0IjoiIiwgImlkIjoiYmUyM2ZkYmUtMmE0My00YjdkLWJiMGEtZGVjZjI0YWJhMzJhIiwgIm5ldCI6IndzIiwgInBhdGgiOiIvZ3JhcGhxbCIsICJwb3J0IjoiODAiLCAicHMiOiJ2MnJheSIsICJ0b
```

### If you want to use a proxt server:
Configure iptables:
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination DEST_SERVER:80
sudo iptables -t nat -A POSTROUTING -j MASQUERADE
sudo iptables-save
```
Activate forwarding edit `/etc/sysctl.conf` and uncomment this line:
```
net.ipv4.ip_forward=1
```
Finally:
```
sudo sysctl -p
```
