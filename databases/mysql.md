# MySQL cheatsheet by Ehsan Shirzadi

### Install only mysql client:
```
apt install mysql-client
```

### Connect to mysql instance (consider there is no space after -h -u -p):
```
mysql -hHOST_IP --port 30671 -uroot -pPASSWORD
```

### Backup database:
```
mysqldump -hHOST --port 3306 -uUSER -pPASSWORD DATABASE > backup.sql
mysqldump -hService.Namespace.svc.cluster.local --port 3306 -uUSER -pPASSWORD DATABASE > backup.sql # k8s way
```
### Restore database:
```
mysql -hHOST --port 3306 -uUSER -pPASSWORD DATABASE < backup.sql
```


Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
