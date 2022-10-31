# How to renew kubernetes certificates?
Step 1: Check certificate's current expiration date:
```
kubeadm certs check-expiration
```
Step 2: Renew all certificates
```
kubeadm certs renew all
```


### References: 
- [Certificate Management with kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#:~:text=You%20can%20renew%20your%20certificates,restart%20the%20control%20plane%20Pods)
