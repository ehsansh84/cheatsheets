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
kubectl create secret tls my-tls-secret --cert=path/to/cert/file --key=path/to/key/file 
```


Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
