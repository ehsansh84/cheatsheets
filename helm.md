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


Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
