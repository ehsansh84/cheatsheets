# How to renew kubernetes certificates?
Step 1: Check certificate's current expiration date:
```
kubeadm certs check-expiration
```
Step 2: Renew all certificates
```
kubeadm certs renew all
```
Step 3: Restart static pods:
To restart a static Pod you can temporarily remove its manifest file from `/etc/kubernetes/manifests/` and wait for 20 seconds
```
cd /etc/kubernetes/manifests/
mkdir ../temp
mv * ../temp
# wait a few seconds
mv ../temp/* .
```
Now you can see there are newly created pods:
```
docker ps
```


### References: 
- [Certificate Management with kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#:~:text=You%20can%20renew%20your%20certificates,restart%20the%20control%20plane%20Pods)
