# How to run a V2Ray server?
## Method 1:
```
sudo apt update
sudo apt install docker.io
sudo apt install docker-compose
wget https://raw.githubusercontent.com/SonyaCore/vmess-deploy/main/deploy.sh
bash deploy.sh
```
Copy the output into your v2ray client, something like this:
```
vmess://eyJhZGQiOiIxNjcuMjM1LjE1Ny4yMDgiLCAiYWlkIjoiMCIsICJob3N0IjoiIiwgImlkIjoiYmUyM2ZkYmUtMmE0My00YjdkLWJiMGEtZGVjZjI0YWJhMzJhIiwgIm5ldCI6IndzIiwgInBhdGgiOiIvZ3JhcGhxbCIsICJwb3J0IjoiODAiLCAicHMiOiJ2MnJheSIsICJ0b
```
