# Helm cheatsheet by Ehsan Shirzadi

### Install helm:
```
sudo snap install helm --classic
```


### Install helm from apt:
```
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```
### To search for helm repositories click on:
https://artifacthub.io/

### See list of repos:
```
helm repo list
```

### Add a new repo:
```
helm repo add name url
```


### Update repos:
```
helm repo update
```

### Search for repos:
```
helm search repo partial_name
```

### Install helm chart:
```
helm install name directory
```



Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
