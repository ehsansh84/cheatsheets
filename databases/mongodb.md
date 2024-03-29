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

### MongoDB SELECT COUNT GROUP BY With conditions:
```
db.contest.aggregate([
    {"$match": {}},
    {"$group" : {_id:"$province", count:{$sum:1}}}
])
```

### mongoexport using queu":
```
 mongoexport --db newshub --collection news --out news_small.json --query '{"status": "summary"}'
 mongoexport --db newshub --collection news --out news_small.json --query '{"status": "summary", "create_date": {"$gt": {"$date": "2021-01-14T11:56:13.248Z"}}}'
 ```

### Create an admin user:
```
use admin

db.createUser({
    user: 'root',
    pwd: 'roosh',
    roles: [
            { role: "root", db: "admin" },
            { role: "userAdminAnyDatabase", db: "admin" },
            { role: "dbAdminAnyDatabase", db: "admin" }
    ],
});
```
In this case AUTH_DATABASE is admin and connection URI will be:
```
mongodb://USERNAME:PASSWORD@HOST:PORT/AUTH_DATABASE
```


If you want to apply authentication in mongodb, you must run mongodb using --auth switch.
If it is running inside a docker-compose, do it like this:
```yaml
version: '3.3'
services:
  mongodb:
    container_name: mongodb
    image: mongo
    restart: unless-stopped
    ports:
      - 27027:27017/tcp
    volumes:
      - /volumes/mongodb/data:/data/db
    command: --auth
```
