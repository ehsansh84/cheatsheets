# Install latest kubernetes on Debian

### Install docker
```commandline
sudo apt update
sudo apt upgrade
sudo apt install docker.io
sudo systemctl enable docker
sudo systemctl start docker
```

### Install Kubernetes Components
```commandline
sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

In case you need, install `gnupg`:
```commandline
sudo apt-get install gnupg
```

### Disable Swap
```commandline
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sudo swapoff -a
```

### Simple init
```
sudo kubeadm init
```
If you want to use config file `config.yaml`, You can create it this like this:
```yaml
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
imageRepository: CUSTOM_IMAGE_REPO
kubernetesVersion: v1.27.3
controlPlaneEndpoint: CONTROL_PLANE_ENDPOINT:6443
---
kind: KubeletConfiguration
apiVersion: kubelet.config.k8s.io/v1beta1
cgroupDriver: systemd
```
And run:
```
sudo kubeadm init --config config.yaml
```
