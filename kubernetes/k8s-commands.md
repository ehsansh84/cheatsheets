# Kubernetes commands cheatsheet by Ehsan Shirzadi

### Label nodes:
```
kubectl label node node_name node-role.kubernetes.io/label=
```

### Remove Label from nodes:
```
kubectl label node node_name node-role.kubernetes.io/label-
```
### Exec into a multi container pod:
```
kubectl exec -it pod_name -c container_name --  bash
```
### Create a tls secret:
```
kubectl create secret tls my-secret-name --cert=path/to/cert/file --key=path/to/key/file 
```
### Read last 10 logs:
```
kubectl logs --tail=20 nginx
```
### Port forwarding:
```
kubectl port-forward pod_name local_port:pod_port
```
### Create secret for TLS:
```commandline
kubectl create secret tls my-tls-secret --cert=fullchain.pem --key=priv.pem
```
### Force delete all pods:
```commandline
kubectl delete -n argocd po --grace-period=0 --force --all
```
### Embed certificates inside kube.config
```commandline
kubectl config view --flatten > kube.config
```
### Taint a node:
```
kubectl taint nodes node1 storage-node=true:NoSchedule
```
### Remove taint (Only add a `-` at the end):
```
kubectl taint nodes node1 storage-node=true:NoSchedule-
```
### Create secret from certificate:
```
kubectl create secret tls secret_name --cert=fullchain.pem --key=private.key -n namespace
```

### Clean Up Old Containers and Images
edit: `/var/lib/kubelet/kubeadm-flags.env` and add:
```commandline
KUBELET_KUBEADM_ARGS="--image-gc-high-threshold=60 --image-gc-low-threshold=50"
```
After editing the file, restart Kubectl:
```commandline
systemctl daemon-reload
systemctl restart kubelet
```
### Set default storage class:
```
kubectl patch storageclass storage_class_name -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```
### Unset default storage class:
```
kubectl patch storageclass storage_class_name -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
```
### Get metrics:
```
kubectl top pods
kubectl top nodes
```
### Images pull:
```
kubeadm config images pull
```
### References:
- [How to Clean Up Old Containers and Images in Your Kubernetes Cluster](https://www.howtogeek.com/devops/how-to-clean-up-old-containers-and-images-in-your-kubernetes-cluster/)
- [How to find available resources in a Kubernetes Cluster level?](https://stackoverflow.com/questions/59212544/how-to-find-available-resources-in-a-kubernetes-cluster-level)
- []()
- []()
