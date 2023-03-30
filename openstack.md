A sample of openstack cloud config
```yaml
#cloud-config
system_info:
  default_user:
    name: ubuntu
    lock_passwd: true
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
password: YOUR_PASSWORD
chpasswd: { expire: False }
ssh_pwauth: True
ssh_authorized_keys:
  - ssh-rsa YOUR KEY
  ```
