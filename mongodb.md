# MongoDB cheatsheet by Ehsan Shirzadi

### Want allways pretty print in mongo shell?
edit `$HOME/.mongorc.js` to enable pretty print globally by default.
```
DBQuery.prototype._prettyShell = true
```

### Create a role:
```
db.createRole({role : 'my_role', privileges : [ {resource : {db : "my_db", collection : "my_collection"}, actions : ["find"]}], roles : ["read"]})
```

### Create a user:
```
db.createUser( { user: "my_user", pwd: "my_password", roles: [ { role: "my_role", db: "temp" }] })
```

### MongoDB SELECT COUNT GROUP BY:
```
db.contest.aggregate([
    {"$group" : {_id:"$province", count:{$sum:1}}}
])
```

