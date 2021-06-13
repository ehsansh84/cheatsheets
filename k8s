# Kubernetes cheatsheet by Ehsan Shirzadi

First install docker:
```
apt install docker.io
```

### How to install master:
Run this for all nodes
```
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

### Change native cgroup to systemd
Run this for all nodes
```
cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
```

```
systemctl restart docker
```

### For debian:
```
sysctl -p
```
### To start master:
```
kubeadm init
```
Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
