Run install to install poetry:
```
export PATH="/opt/homebrew/opt/mysql@8.0/bin:$PATH"
export MYSQL_HOME="/opt/homebrew/opt/mysql@8.0/include"
export MYSQLCLIENT_CFLAGS="-I/opt/homebrew/opt/mysql@8.0/include/mysql/"
export MYSQLCLIENT_LDFLAGS="-L/opt/homebrew/opt/mysql@8.0/lib -lmysqlclient"

/Users/ehsanshirzadi/Library/Python/3.9/bin/poetry install
```
