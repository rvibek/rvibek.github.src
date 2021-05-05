Title: Setting up Docker in ArubaCloud
Slug: setting-up-docker-in-arubacloud
Date: 2018-07-20 08:25:16
Modified: 2020-02-20 22:45:14
Tags: docker, aruba, python, nginx, jupyter, data science
Category: Blog
Author: Vibek Raj Maurya
Lang: 
Summary: Experimenting a multiple of instance of dockers in arubacloud VPS using docker-machine aruba driver

I have been using  [arubacloud](https://www.arubacloud.com) VPS for some time now. Price wise, it's cheap and can't complain about the service. The subscription is as low as 1 EUR/month for 1 vCPU, 1 GB RAM, 20 GB SSD Storage and 2 TB/month data transfer.

This is an experiment to setup a multiple of instance of dockers in a VPS using [docker-machine aruba driver](https://github.com/Arubacloud/docker-machine-driver-arubacloud). I have 2 docker instances running - [jupyter/datascience-notebook](https://hub.docker.com/r/jupyter/datascience-notebook/) and [nginx](https://hub.docker.com/_/nginx/)

Creating a new server is straightforward


```
docker-machine ssh arubadocker
``` 

then to SSH the VPS

and, to create instances of dockers

```
docker pull nginx
docker pull jupyter/datascience-notebook
```

Data science-notebook setups with the default user ```jovyan```, which is not a sudoer.  My attempt to find ```sudo``` password in the internet was in vain. However, I could start the docker as a root from the host. It allows me to install/update software. 

```
docker run --name jupyter-dockr  -p 8888:8888 -p 2223:22 -e GRANT_SUDO=yes --user root -d  jupyter/datascience-notebook 
```

