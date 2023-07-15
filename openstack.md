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
  
After the instance initiated, you can find this config here:
```/var/lib/cloud/instance/cloud-config.txt```

You can get ip of instance from inside:
```
instance_ip=$(curl -s http://169.254.169.254/latest/meta-data/local-ipv4)
```

You can get UUID of instance from inside:
```
instance_uuid=$(curl -s http://169.254.169.254/openstack/latest/meta_data.json | grep -oP '"uuid": "\K[^"]+')
```
Another way to get instance_id:
```
cloud-init query v1.instance_id
```
Full cloud-config is here:
```
/etc/cloud/cloud.cf
```
You can see cloud-init logs:
```
tail -f /var/log/cloud-init-output.log
```
Re-run cloud-init:
```
systemctl restart cloud-init.service
```
Install openstack cli:
```
pip install python-openstackclient
```
Install octavia for openstack cli
```
pip install python-octaviaclient
```
