# KinD (Kubernetes in Docker) cheatsheet by Ehsan Shirzadi

### Install kubectl:
```
sudo snap install kubectl --classic
```

### Install docker
``` 
apt install docker.io
```

### Install kind:
```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
chmod +x ./kind
mv ./kind /usr/bin
kind version
```

### Create a cluster:
```
kind create cluster # using default name
kind create cluster --name cluster_name # specifying name
```

### Delete a cluster:
```
kind delete cluster –name <cluster name>
```


Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
