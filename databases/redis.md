# Redis cheatsheet
### Install only redis client:
```
sudo apt install redis-tools
```
### Connect to a remote redis instance:
```
redis-cli -h host -p port
redis-cli -h host -p port -a password
redis-cli -u redis://password@host:port
redis-cli -u redis://username:password@host:port
```


### References:
- [How to connect to remote Redis server?](https://stackoverflow.com/questions/40678865/how-to-connect-to-remote-redis-server)
- [Linux - Install redis-cli only](https://stackoverflow.com/questions/21795340/linux-install-redis-cli-only)
- []()
 
