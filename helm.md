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



| Command          | Description                         |
| ---------------- |:-----------------------------------:|
| `helm repo list` | List of repos |
| `helm repo add name url` | Add a new repo |
| `helm repo update` | Update repos |
| `helm search repo partial_name` | Search for repos |
| `helm install name directory` | Install helm chart |
| `helm uninstall name` | Uninstall helm chart |
| `helm uninstall name --keep-history` | Uninstall helm chart but keeps history |
| `helm install name directory --set param1=value1, param2=value2` | Install helm chart with params |
| `helm upgrade name directory --set param1=value1` | Update params (Other params will reset) |
| `helm upgrade name directory --set param1=value1 --reuse-values` | Update params (Other params will not reset) |
| `helm get notes name` | View notes inside chart |
| `helm lint directory` | Check the syntax |
|  |  |









Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
