# How to backup kubernetes using Velero?  

### Step 1: download velero binaries:
```commandline
wget https://github.com/vmware-tanzu/velero/releases/download/v1.8.1/velero-v1.8.1-linux-amd64.tar.gz
tar xvfz velero-v1.8.1-linux-amd64.tar.gz
sudo mv velero /usr/local/bin/
```
### Step 2: Create credential file named `credentials-minio`:
```commandline
[default]
aws_access_key_id = XXXXXXXXXX
aws_secret_access_key = YYYYYYYYYY
```
### Step 3:
Install velero:
```commandline
velero install \
 --provider aws \
 --plugins velero/velero-plugin-for-aws:v1.0.0 \
 --bucket iranserver  \
 --secret-file ./credentials-minio  \
 --use-volume-snapshots=true \
 --backup-location-config region=default,s3ForcePathStyle="true",s3Url=http://MY_S3_STORAGE_IP  \
 --image velero/velero:v1.4.0  \
 --snapshot-location-config region="default" \
 --use-restic
```
### Step 4: Perform a namespace backup
```
velero backup create backup_name --include-namespaces namespace_name
```

# How to restore backups?
### Get the list of backups:
```
velero backup get
```
Restore backup:
```
velero restore create --from-backup backup_name
```
