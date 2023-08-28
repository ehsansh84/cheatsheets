# Sending logs using filebeat

Install filebeat:
```
wget https://mirror.iranserver.com/elk/filebeat-oss-8.2.0-amd64.deb
sudo dpkg -i filebeat-oss-8.2.0-amd64.deb
```
Edit config file `/etc/filebeat/filebeat.yml`
```yaml
# ============================== Filebeat inputs ===============================

filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /home/oem/dev/cman-celery/logs/*.log
  exclude_files: ['.gz$']
  fields:
    type: cman
  fields_under_root: true

# ============================== Filebeat modules ==============================

filebeat.config.modules:
  # Glob pattern for configuration loading
  path: ${path.config}/modules.d/*.yml

  # Set to true to enable config reloading
  reload.enabled: false

  # Period on which files under path should be checked for changes
  #reload.period: 10s

# ================================== Outputs ===================================

# ------------------------------ Logstash Output -------------------------------
output.logstash:
  hosts: ["172.20.11.11:5050"]

# ================================= Processors =================================
processors:
  - add_host_metadata:
      when.not.contains.tags: forwarded
  - add_cloud_metadata: ~
  - add_docker_metadata: ~
  - add_kubernetes_metadata: ~
```
Restart the service:
```
sudo systemctl restart filebeat.service
```
