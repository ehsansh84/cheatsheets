# How to use registry secrets in kubernetes?

### Step1: Do a docker login on a machine
```
docker login registry.dockerhost.com
```
### Step2: Convert your auth data to base64
```
cat ~/.docker/config.json | base64 -w 0
```
### Step3: Create a secret
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: registry-secret
  namespace: namespace
data:
  .dockerconfigjson: your_base64_data
type: kubernetes.io/dockerconfigjson
```

### Setp 4: Use it in your `imagePullSecrets`
```yaml
spec:
  imagePullSecrets:
  - name: registry-secret 
```
