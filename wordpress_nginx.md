# Installation of wordpress on nginx by Ehsan Shirzadi

When creating a Mysql user, You should change the password authentication plugin to: Native Mysql Authentication

### Set the owner to www-data:
```
chown -R www-data:www-data path_to_website_root
```

### If needed set permissions:
```
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \; 
```

Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
