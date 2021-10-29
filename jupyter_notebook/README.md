## Build Image
```
$ docker build -t [image name] .
```
builds image in current directory.
## Initialize Container
```
$ docker run -it -p 9999:8888
```
initializes the container
## Restart Container
```
$ docker start -ia [container]
```