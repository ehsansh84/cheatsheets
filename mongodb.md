# MongoDB cheatsheet by Ehsan Shirzadi

### Create a role:
```
db.createRole({role : 'my_role', privileges : [ {resource : {db : "my_db", collection : "my_collection"}, actions : ["find"]}], roles : ["read"]})
```

### Create a user:
```
db.createUser( { user: "my_user", pwd: "my_password", roles: [ { role: "my_role", db: "temp" }] })
```
