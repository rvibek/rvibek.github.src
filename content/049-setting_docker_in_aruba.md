Title: Setting up Docker in ArubaCloud
Slug: setting-up-docker-in-arubacloud
Date: 2018-07-20 08:25:16
Modified: 2018-07-20 22:45:14
Tags: docker, aruba, python, nginx, jupyter
Category: Blog
Author: Vibek Raj Maurya
Lang: 
Summary: I am experimenting a multiple of intances of dockers in a vps using docker-machine aruba driver

I have been using  [arubacloud](https://www.arubacloud.com) VPS for sometime now. Price wise, it's cheap and the service is good. Their price is as low as 1 Euro/month with 1 vCPU, 1 GB RAM, 20 GB SSD Storage and 2 TB/month data transfer.

I am experimenting a multiple of intances of dockers in a vps using [docker-machine aruba driver](https://github.com/Arubacloud/docker-machine-driver-arubacloud). I have 2 docker instances running - [jupyter/datascience-notebook](https://hub.docker.com/r/jupyter/datascience-notebook/) and [nginx](https://hub.docker.com/_/nginx/)

Creating a new server is straight forward

```
docker-machine create --driver arubacloud \
 --ac_action "NewSmart"\
 --ac_username                    "AWI-XXXX" \
 --ac_password                    "XXXXXX" \
 --ac_endpoint                    "dc1" \
 --ac_template                    "ubuntu1604_x64_1_0" \
 --ac_size                        "Large" \
 --ac_admin_password              "XXXXXX" arubdocker
```

then ```docker-machine ssh arubadocker``` to SSH the vps

and, to create instances of dockers

```
docker pull nginx
docker pull jupyter/datascience-notebook
```

Datascience-notebook setups with the default user ```jovyan```, which is not sudoer.  My attempt to find ```sudo``` password was invain. However, I could start the docker as a root from the host. It allows me to install/update software. 

```docker run --name jupyter-dockr  -p 8888:8888 -p 2223:22 -e GRANT_SUDO=yes --user root -d  jupyter/datascience-notebook ```