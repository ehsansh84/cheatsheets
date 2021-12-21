# Postgresql cheatsheet by Ehsan Shirzadi

### Drop database force:
```
dropdb keycloak --force;
```

### Install only postgres client:
```
sudo apt-get install postgresql-client
psql
```
### Connect to postgres inside anoyher namespace on k8s:
```
psql -h service_name.namespace -p 5432 -U postgres postgres
```
Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
