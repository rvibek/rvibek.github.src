Title: Create and install Ghost 
Slug: create-and-install-ghost
Date: 2021-08-12 21:20
Modified: 2021-08-12 21:20
Tags: ghost, site generator, node, git
Category: Blog
Author: Vibek Raj Maurya
Lang: en

Summary: A quick note on setting up Ghost CMS locally and using wget command to generate required resources to host it in Github. 


I had migrated this site from [WordPress to Ghost](https://rvibek.com.np/new-blog-again-EN.html) in 2015. I maintained it in Ghost until [OpenShift](https://www.openshift.com/) allowed three free containers. Later, the site was migrated to [Pelican](https://getpelican.com/), partially for the love of Python. Well essentially, I had to find a hosting alternative as the OpenShift was discontinuing free service. 


I  might switch back to [Ghost](https://github.com/TryGhost/Ghost) headless CMS. Until I do so, let me try to log the process - I have already tried in the local machine, I am yet to work on the theme.

The first step is to grab [Ghost CLI](https://ghost.org/docs/ghost-cli/)

```
# On a production server using a non-root user:
sudo npm install -g ghost-cli@latest
# or
sudo yarn global add ghost-cli@latest
```

Since the system encountered a problem with the Node.js version, I created isolated node.js environments [nodeenv](https://pypi.org/project/nodeenv/).  

```
nodeenv --node=14.16.1 node14161
 . node14161/bin/activate
```

Once it is installed, ```cd``` inside the folder where the Ghost will reside the fire.

```
ghost install local
```
...and the configuration follows

When I finalise templating, I should ```wget``` the localhost from ```themes``` folder to extract HTML, CSS and javascript which then can then be uploaded to the Github  repository

```
wget -r -nH -P docs -E -T 2 -np  -k http://localhost:2368/
```






