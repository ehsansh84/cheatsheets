# Docker cheatsheet by Ehsan Shirzadi

### Install docker engine on Debian:
```
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```

### Images:
##Pull new image:
```
sudo docker pull image_name
```

##See images list:
```
sudo docker images
```

##Docker stop container:
```
sudo docker stop container_id
```

##Docker build (use it inside the folder containing DockerFile):
```
sudo docker build -t name:tag
```

##Get into the docker:
```
sudo docker exec -it container_name bash
```



