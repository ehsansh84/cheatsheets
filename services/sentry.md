# Install sentry

To install sentry you need these requirements:
```commandline
- Docker 19.03.6+
- Compose 2.0.1+
- 4 CPU Cores
- 8 GB RAM
- 20 GB Free Disk Space
```
You can install latest docker and docker-compose this way:
```commandline
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh    
```
Or if you already have docker you can get latest docker-compose from this link:
```commandline
https://github.com/docker/compose/releases/
```

After that it is easy to install sentry:
```commandline
git clone https://github.com/getsentry/self-hosted.git
cd self-hosted/
./install.sh 
```

Consider it's a huge project, and it takes a bit long to get installed.
