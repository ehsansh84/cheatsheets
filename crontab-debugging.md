# How to debug cron jobs by Ehsan Shirzadi

### Add `>> /home/cron.log 2>&1 ` after your command like this:
```
* * * * * /usr/bin/docker exec -i test-scripts python /app/cron.py>> /home/cron.log 2>&1 
```
Output will be added to /home/cron.log

### You want to know where is your crontab file?
Look here: `/var/spool/cron/crontabs`


###### Email: Ehsan.Shirzadi@Gmail.com
###### Web: www.ehsanshirzadi.com

