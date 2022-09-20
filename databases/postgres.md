# Postgresql cheatsheet by Ehsan Shirzadi
### Commands:
```
\l # List databases
\df # List functions
\df+ # List functions and source code
\df # List functions
\dy+ # List triggers and source code
\dy <schema>.* # List triggers
\c db_name # connect to a database
\td # List tables
```
### Drop database force:
```
dropdb keycloak --force;
```

### Install only postgres client:
```
sudo apt-get install postgresql-client
psql
```
### Connect to postgres inside another namespace on k8s:
```
psql -h service_name.namespace -p 5432 -U postgres postgres
```
### Backup from postgres:
```
psql -h <host> -p <port> -U <db_user> <database_name>
```
Another way:
```
pg_dump -U <user> -h <host_ip> -p <port> <db_name> > backup.sql
```
If you use above commands, a password will be asked, bypass it like this:
```
export PGPASSWORD="$put_here_the_password"
```
### Create a user:
```
create user user_name with encrypted password 'password';
```
### Grant privilages to user:
```
grant all privileges on database db_name to user_name;
```
### List of all tables:
```
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
```
### List of all triggers:
```
SELECT  * FROM information_schema.triggers;
```

### References:
- (How to pass in password to pg_dump?)[https://stackoverflow.com/questions/2893954/how-to-pass-in-password-to-pg-dump]
